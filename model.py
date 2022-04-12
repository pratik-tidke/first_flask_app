from config import db


class User(db.Model):
    id = db.Column('id', db.Integer(), primary_key=True)
    firstname = db.Column('firstname', db.String(30))
    lastname = db.Column('lastname', db.String(30))
    email = db.Column('email', db.String(30))
    gender = db.Column('gender', db.String(30))
    photo = db.Column('user_photo',db.String(30),default = 'NA')
    loginref = db.relationship('Login',backref = 'userref',uselist=False)

#User(firstname,lastname,email,gender,photo)

class Login(db.Model):
    id = db.Column('id', db.Integer(), primary_key=True)
    username = db.Column('username', db.String(30))
    password = db.Column('password', db.String(1000))
    userid = db.Column('userid',db.ForeignKey('user.id'),unique=True,nullable=False)

#Login(username,password,userid)

class Product(db.Model):
    __tablename__ = "PRODUCT_INFO"
    id = db.Column('PROD_ID',db.Integer(),primary_key=True)
    name = db.Column('PROD_NAME',db.String(30))
    vendor = db.Column('PROD_VENDOR', db.String(30))
    category = db.Column('PROD_CATEGORY', db.String(30))
    price = db.Column('PROD_PRICE', db.Float())
    qty = db.Column('PROD_QTY', db.Integer())

    @staticmethod
    def dummy_product():
        return Product(id=0,name='',qty=0,price=0.0,category='',vendor='')


db.create_all() # this will make sure at the time app start -- tables will be created.