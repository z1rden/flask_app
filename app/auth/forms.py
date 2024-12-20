from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError

from app.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 64),
                            Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                            'Пользователи могут пользоваться только буквами,'
                                                   'цифрами, точками or подчеркиваниями')])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2',
                                                                             'Пароли должны совпадать')])
    password2 = PasswordField('Подтвердите пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Такой email уже зарегистрирован.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Такой пользователь уже зарегистрирован.')

