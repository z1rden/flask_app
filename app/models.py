from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))

    #чтобы не использовать setter'ы и getter'ы, используется декоратор property
    #сначала определяется getter
    @property
    def password(self):
        raise AttributeError('Нельзя прочитать пароль')

    #затем setter (у них обязательно должны быть одинаковые названия функций)
    @password.setter
    def password(self, password):
        password_hash = generate_password_hash(password, method='pbkdf2')
        self.password_hash = password_hash
        #в python, который поставляется с macos, отсутствует scrypt-модуль, поэтому добавляется method
        #https://github.com/miguelgrinberg/microblog/issues/404

    #теперь для ПОПЫТКИ получения значения используется <объект_класса>.password
    #для изменения значения <объект_класса>.password = jdfsajf

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    #Flask - Login отслеживает зарегистрированного пользователя, сохраняя его уникальный идентификатор
    #в пользовательском сеансе Flask, назначенный каждому пользователю, который подключается к приложению.
    #Каждый раз, когда вошедший в систему пользователь переходит на новую страницу, Flask - Login
    #извлекает идентификатор пользователя из сеанса и затем загружает этого пользователя в память.
    #Поскольку Flask - Login ничего не знает о базах данных, ему нужна помощь приложения при загрузке
    #пользователя. По этой причине расширение ожидает, что приложение настроит функцию загрузчика пользователя, которую
    #можно вызвать для загрузки пользователя с идентификатором.

    def __repr__(self):
        return '<User %r>' % self.username