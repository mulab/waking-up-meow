from config import configs
from flask import Flask


def create_app(name):
    app = Flask(__name__)
    app.config.from_object(configs[name])

    # TODO: you should register your blueprint for different router.

    return app
