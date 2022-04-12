from productcontroller import *
from registercontroller import *
from logincontroller import *

@app.route('/index')
def welcome_page():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)