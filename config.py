import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # TODO:

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    # TODO:
    pass

class TestingConfig(Config):
    TESTING = True
    # TODO:
    pass

class ProductionConfig(Config):
    PRODUCTION = True
    # TODO:
    pass

configs = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
