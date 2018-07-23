import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DefaultConfig(object):
    SECRET_KEY = 'secret-key'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' + os.path.join(basedir, 'default.sqlite'))


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' + os.path.join(basedir, 'dev.sqlite'))


config_env_files = {
    'development': 'app.config.DevelopmentConfig',
}
