from flask import request
from flask.views import MethodView

from src.utils import json_response
from src.extensions.authentication import (
    create_user,
    generate_login_token,
    AlreadyRegisteredError,
    InvalidUserError,
    IncorrectPasswordError,
)


class UserAPI(MethodView):
    def post(self):
        """Tries to create a new user"""
        body = request.get_json()
        if body is None:
            return json_response(
                message="A JSON body must be provided",
                status_code=400,
                path=request.full_path,
                method=request.method,
            )

        username = body.get("username", None)
        password = body.get("password", None)

        if username is None:
            return json_response(
                message="Field 'username' must not be empty",
                status_code=400,
                path=request.full_path,
                method=request.method,
            )
        if password is None:
            return json_response(
                message="Field 'password' must not be empty",
                status_code=400,
                path=request.full_path,
                method=request.method,
            )

        try:
            create_user(username=username, password=password)
            return json_response(
                message=f"Created user {username}",
                status_code=201,
                path=request.full_path,
                method=request.method,
            )
        except AlreadyRegisteredError:
            return json_response(
                message="Username already registered",
                status_code=400,
                path=request.full_path,
                method=request.method,
            )

    def get(self):
        """Tries to get user's access token"""
        body = request.args
        username = body.get("username", None)
        password = body.get("password", None)

        if username is None:
            return json_response(
                message="Field 'username' must not be empty",
                status_code=400,
                path=request.full_path,
                method=request.method,
            )
        if password is None:
            return json_response(
                message="Field 'password' must not be empty",
                status_code=400,
                path=request.full_path,
                method=request.method,
            )

        try:
            token = generate_login_token(username=username, password=password)
        except (InvalidUserError, IncorrectPasswordError):
            return json_response(
                # ! Don't say to hackers if it is the username that doesn't
                # ! exists or if the password is incorrect.
                message="Invalid username or password",
                status_code=400,
                path=request.full_path,
                method=request.method,
            )
        else:
            return json_response(
                message="Token successful generated",
                status_code=200,
                path=request.full_path,
                method=request.method,
                payload={"access_token": token},
            )
