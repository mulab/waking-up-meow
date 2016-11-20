from flask import Blueprint

helper_blueprint = Blueprint(__name__, 'helper')


@helper_blueprint.route('/', methods=['GET'])
def helper():
    return 'Hello World'

# TODO: you can add other useful method you think in helper
