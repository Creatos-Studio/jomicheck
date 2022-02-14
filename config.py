import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    # SECRET_KEY = 'kjñlasdflkjñkjfsldña'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevelopmentConfig(Config):
    ENV = 'development'
    DEVELOPMENT =  True
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = 'mariadb+pymysql://lalo:password@localhost:3306/jomicheck'
    # SQLALCHEMY_DATABASE_URI = 'mysql://lalo:password@localhost:3306/jomicheck'
