import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    LOG_LEVEL = 'DEBUG'
    LOG_DIR = basedir
    LOG_FILE = "production.log"
    DEBUG = False


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    LOG_LEVEL = "DEBUG"
    LOG_DIR = basedir
    LOG_FILE = "development.log"

