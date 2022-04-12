from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/mvcapp'
app.config['SECRET_KEY'] = '1289asjdkl7*&@H1237iJDHY*#'
#app.config['SQLALCHEMY_ECHO']=True      # print sql statements-- created by sqlalchemy.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False  # dont show warnings

db = SQLAlchemy(app)