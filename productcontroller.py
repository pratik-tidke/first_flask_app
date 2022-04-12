from config import *
from model import Product
from flask import session

@app.route('/product/save/', methods = ['POST','GET'])    #http://localhost:5000/product/save/
def save_product_information():
    if session.get('user_name'):
        msg = ''

        reqdata  = request.form         #immutable dict --> key:        pid:101     pnm:"ABCD"
        if reqdata:
            dbprod = Product.query.filter_by(id=reqdata.get('pid')).first()
            if dbprod:
                #msg = "Duplicate Id Given..!"
                dbprod.name = reqdata.get('pname')
                dbprod.qty = reqdata.get('pqty')
                dbprod.price = reqdata.get('pprice')
                dbprod.vendor = reqdata.get('pven')
                dbprod.category = reqdata.get('pcat')
                db.session.commit()     # update sathi..
                msg = "Product Updated Successfully...!"
                return render_template('listprod.html',
                                       products=Product.query.all())
            else:
                prod = Product(id=reqdata.get('pid'),
                        name=reqdata.get('pname'),
                        qty=reqdata.get('pqty'),
                        price=reqdata.get('pprice'),
                        vendor=reqdata.get('pven'),
                        category=reqdata.get('pcat'))
                db.session.add(prod)        # insert query will be fired..
                db.session.commit()         # data will be committed
                msg = "Product Added Successfully...!"
                #prod = Product.dummy_product()  #empty

            #prod_list = Product.query.all()
        return render_template('saveprod.html',resp = msg,product = Product.dummy_product(),
                               products = Product.query.all(),name = session['user_name'])
    else:
        return render_template('login.html')

@app.route("/delete/<int:pid>",methods = ['GET'])
def delete_product(pid):
    if session.get('user_name'):
        msg = ''
        dbprod = Product.query.filter_by(id=pid).first()
        if dbprod:
            db.session.delete(dbprod)
            db.session.commit()
            msg = "Product Deleted Successfully...!"
        return render_template('listprod.html', resp=msg, product=Product.dummy_product(),
                               products=Product.query.all(),name = session['user_name'])
    else:
        return render_template('login.html')

@app.route("/edit/<int:pid>",methods = ['GET'])
def populate_data_in_form_for_edit(pid):
    if session.get('user_name'):
        dbprod = Product.query.filter_by(id=pid).first()
        return render_template('updateprod.html', resp='', product=dbprod, products=Product.query.all(),
                               name = session['user_name'])

    else:
        return render_template('login.html')

@app.route("/showall",methods = ['GET'])
def show_all_products():
    if session.get('user_name'):
        return render_template('listprod.html', resp='', products=Product.query.all(),name = session['user_name'])
    else:
        return render_template('login.html')