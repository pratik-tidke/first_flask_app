from config import *
from model import *
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/register",methods = ['GET','POST'])
def user_registration():
    message = ''
    if request.method == 'POST':
        formdata = request.form

        loginrecord = Login.query.filter(Login.username==formdata.get('username')).first()
        if loginrecord:
            message = "Username Already Exist"
        else:
            user = User(firstname=formdata.get('firstname'),
                 lastname=formdata.get('lastname'),
                 email=formdata.get('email'),
                 gender=formdata.get('gender'))
            db.session.add(user)
            db.session.commit()

            login  = Login(username = formdata.get('username'),password=generate_password_hash(formdata.get('password')),userid = user.id)
            db.session.add(login)
            db.session.commit()
            message = "User successfully Registered"

    return render_template('register.html',result = message)



