from flask import request
from flask.views import MethodView

from src.utils import json_response
from src.extensions.authentication import create_user, AlreadyRegisteredError


class UserAPI(MethodView):
    def post(self):
        body = request.get_json()
        if body is None:
            return json_response(
                message="A JSON body must be provided",
                status_code=400,
                path=request.full_path,
            )

        username = body.get("username", None)
        password = body.get("password", None)

        if username is None:
            return json_response(
                message="Field 'username' must not be empty",
                status_code=400,
                path=request.full_path,
            )
        if password is None:
            return json_response(
                message="Field 'password' must not be empty",
                status_code=400,
                path=request.full_path,
            )

        try:
            create_user(username=username, password=password)
            return json_response(
                message=f"Created user {username}",
                status_code=201,
                path=request.full_path,
            )
        except AlreadyRegisteredError:
            return json_response(
                message="Username already registered",
                status_code=400,
                path=request.full_path,
            )
