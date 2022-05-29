import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://code_monkey:gerrit@localhost/fyurr'
SECRET_KEY = os.urandom(32)

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://code_monkey:gerrit@localhost/fyurr'
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://code_monkey:gerrit@localhost/fyurr'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}