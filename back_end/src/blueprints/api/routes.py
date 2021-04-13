from flask import Blueprint
from .resources import UserAPI

user_view = UserAPI.as_view("user_api")


def init_app(bp: Blueprint):
    bp.add_url_rule(
        "/users/",
        view_func=user_view,
        methods=["POST", "GET"],
    )
