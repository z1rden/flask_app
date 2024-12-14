from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
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
        password_hash = generate_password_hash(password)

    #теперь для ПОПЫТКИ получения значения используется <объект_класса>.password
    #для изменения значения <объект_класса>.password = jdfsajf

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username