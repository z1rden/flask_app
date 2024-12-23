from flask import render_template
from . import auth

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template('auth/login.html')
    #стоит обратить внимание, что сама папка auth будет находиться в папке templates