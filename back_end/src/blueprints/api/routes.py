from flask import Blueprint
from src.blueprints.api.resources import UserAPI, ContactsAPI

user_view = UserAPI.as_view("user_api")
contacts_view = ContactsAPI.as_view("contacts_api")


def init_app(bp: Blueprint):
    bp.add_url_rule(
        "/users/",
        view_func=user_view,
        methods=["POST", "GET"],
    )
    bp.add_url_rule(
        "/contacts/",
        view_func=contacts_view,
        methods=["GET"],
    )
