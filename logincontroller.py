from config import *
from flask import session
from model import Login
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/login/',methods = ['GET','POST'])
def authenticate_user():
    message = ''
    if request.method == 'POST':
        formdata = request.form
        username = formdata.get('user')
        password = formdata.get('pwd')
        userRecord = Login.query.filter(Login.username == username).first()   #dbrecord
        if userRecord and check_password_hash(userRecord.password,password):
            session['user_name'] = userRecord.username
            return render_template('home.html',name = session['user_name'])
        else:
            message = 'Invalid Credentials'

    return render_template('login.html', message = message)


@app.route('/home')
def home_page():
    if session.get('user_name'):
        return render_template('home.html',name = session['user_name'])
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    if session['user_name']:
        session.pop('user_name')

    return render_template('login.html')
