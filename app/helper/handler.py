from app.helper import helper_blueprint


@helper_blueprint.route('/', methods=['GET'])
def helper():
    return 'Hello World'

# TODO: you can add other useful method you think in helper
