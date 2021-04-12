from flask import Flask
from src.extensions.configuration import configure


def create_app() -> Flask:
    app = Flask(__name__)
    configure(app)
    return app
