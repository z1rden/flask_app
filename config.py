import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    """В будущем для использования почты
    
    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 465
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
                   ['true', 'on', '1']
    MAIL_USERNAME = 'arseniykulagin@yandex.ru'
    MAIL_PASSWORD = 'rowyourboat1'

    #FLASKY_MAIL_SUBJECT_PREFIX = '[Flask-app]'
    #FLASKY_MAIL_SENDER = 'Flask-app Admin <flask-app@example.com>'
    #FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')"""

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
