from functools import wraps
from os import getenv
from time import time

import jwt
from flask import request
from werkzeug.security import check_password_hash, generate_password_hash

from src.utils import json_response
from src.extensions.database import db


class InvalidUserError(Exception):
    pass


class IncorrectPasswordError(Exception):
    pass


class AlreadyRegisteredError(Exception):
    pass


def token_required(func: callable) -> callable:
    """Protect a view requiring an access token

    `ATTENTION`: The view must receive **kwargs

    Parameters
    ----------
    func : callable
        The function to be protected

    Returns
    -------
    callable
        The protected function
    """

    @wraps(func)
    def inner(*args, **kwargs):
        token = request.args.get("access_token", None)
        if not token:
            body = request.get_json()
            if body is not None:
                token = body.get("access_token", None)
        if not token:
            return json_response(
                status_code=401,
                message="An access_token parameter must be provided",
                path=request.full_path,
                method=request.method,
            )

        try:
            token_information = jwt.decode(
                token, getenv("SECRET_KEY"), algorithms=["HS256"]
            )
        except jwt.ExpiredSignatureError:
            return json_response(
                status_code=401,
                message="Expired access_token",
                path=request.full_path,
                method=request.method,
            )
        except jwt.InvalidTokenError:
            return json_response(
                status_code=403,
                message="Invalid access_token",
                path=request.full_path,
                method=request.method,
            )
        except Exception:
            return json_response(
                status_code=500,
                message="Error processing access_token",
                path=request.full_path,
                method=request.method,
            )

        return func(*args, **kwargs, token_information=token_information)

    return inner


def create_user(username: str, password: str):
    """Creates a new user

    Parameters
    ----------
    username : str
        The username of the new user
    password : str
        The password of the new user

    Raises
    ------
    AlreadyRegisteredError
        If the username is already registered
    """
    if db.child("users").child(username).get().each() is not None:
        raise AlreadyRegisteredError("Username already registered!")

    hashed_password = generate_password_hash(password)
    db.child("users").child(username).set({"password": hashed_password})


def generate_login_token(username: str, password: str) -> bytes:
    """Generates a login token for a given user

    Checks the username and password in database
    If they are ok, creates and returns a web token valid for 30 minutes
    The SECRET_KEY env var is used as the jwt encoding key

    Parameters
    ----------
    username : str
        The username to generate a token from
    password : str
        The user's password

    Returns
    -------
    bytes
        Token: `jwt.encode()` response

    Raises
    ------
    InvalidUserError
        If the user doesn't exists
    IncorrectPasswordError
        If the password is incorrect
    """
    if db.child("users").child(username).get().each() is None:
        raise InvalidUserError()

    user_passord = (
        db.child("users").child(username).child("password").get().val()
    )
    if not check_password_hash(user_passord, password):
        raise IncorrectPasswordError()

    token = jwt.encode(
        {
            "username": username,
            "exp": time() + (30 * 60),
        },
        key=getenv("SECRET_KEY"),
    )
    return token
