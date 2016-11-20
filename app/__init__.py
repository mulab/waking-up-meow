from config import configs
from flask import Flask


def create_app(name):
    app = Flask(__name__)
    app.config.from_object(configs[name])

    from app.helper import helper_blueprint
    if app.config.get('PRODUCTION') == False:
        # You can use `app.config` to get runtime enviroment
        app.register_blueprint(helper_blueprint, url_prefix='/helper')

    # TODO: you should register your blueprint for different router.

    return app
