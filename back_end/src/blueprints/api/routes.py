from flask import Blueprint
from src.blueprints.api.resources import UserAPI, UserTokenAPI, ContactsAPI

user_view = UserAPI.as_view("user_api")
user_token_view = UserTokenAPI.as_view("user_token_api")
contacts_view = ContactsAPI.as_view("contacts_api")


def init_app(bp: Blueprint):
    bp.add_url_rule(
        "/users/",
        view_func=user_view,
        methods=["POST"],
    )
    bp.add_url_rule(
        "/user/token/",
        view_func=user_token_view,
        methods=["POST"],
    )
    bp.add_url_rule(
        "/contacts/",
        view_func=contacts_view,
        methods=["POST", "GET"],
    )
