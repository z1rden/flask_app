from threading import Thread
from flask import render_template, current_app
from flask_mail import Message
from . import mail

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)
        #функция mail.send() блокирует работу приложения на несколько секунд, пока письмо не будет отправлено, что
        #создает ощущение зависания браузера. Чтобы избежать нежелательных задержек в процессе обработки запроса,
        #функцию отправки электронной почты можно выполнять в фоновом потоке.

        #функция send() из расширения Flask-Mail использует current_app, поэтому ее следует вызывать только после
        #активации контекста приложения.

def send_email(to, subject, template, **kwargs):
    #current_app всегда здесь будет определен, потому что эта функция работает всегда в контексте запроса
    msg = Message(subject, sender = current_app.config['MAIL_USERNAME'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)

    thr = Thread(target = send_async_email, args = [current_app._get_current_object(), msg])
    thr.start()

    return thr