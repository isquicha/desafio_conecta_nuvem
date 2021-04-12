from datetime import datetime, timedelta
from functools import wraps
from os import getenv

import jwt
# from flask import Flask, request  # noqa
from werkzeug.security import check_password_hash, generate_password_hash

from .database import db


class InvalidUserError(Exception):
    pass


class IncorrectPasswordError(Exception):
    pass


# TODO: Create token required function
def token_required(func: callable) -> callable:
    @wraps(func)
    def inner(*args, **kwargs):
        pass
        # token = request.args.get("access_token", None)
        # try:
        #    pass
        # jwt.decode(token, app.config)
        # except:
        #    pass

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
    RuntimeError
        If the username is already registered
    """
    if db.child("users").child(username).get().each() is not None:
        raise RuntimeError("Username already registered!")

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
            "exp": datetime.utcnow() + timedelta(minutes=30),
        },
        key=getenv("SECRET_KEY"),
    )
    return token
