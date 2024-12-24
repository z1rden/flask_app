import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 465
    # при подключении к серверу по tls или ssl протоколам используются разные порта: ssl - 465, tls - 25, 587
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # пароль, что тут используется, должен отдельно генерироваться в вашей почте, если ранее этого не было сделано
    # то есть это не тот пароль, что используется для входа в почту через web яндекс почту или приложение яндекс почта
    # а пароль для внешних приложений

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
