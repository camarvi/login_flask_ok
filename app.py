

from flask import Flask,redirect,request,session, render_template, url_for, redirect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from forms import LoginUsuario
from models import User

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.config['SECRET_KEY'] = "lkkajdghdadkglajkgah"

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)
    #return User.get_by_id(int(user_id))

#class User(UserMixin):
#  def __init__(self,id):
#    self.id = id


#@app.route('/')
#def home():
#    return "home: <a href='/login/'>Login</a> <a href='/protected/'>Protected</a> <a href='/logout/'>Logout</a>"

@app.route('/' , methods=["GET", "POST"])
def index():
    
    form = LoginUsuario()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        print (name)
        print (password)
        #user = User.get_by_email(form.email.data)
        #if user is not None and user.check_password(form.password.data):
        if (name == 'carlos' and password == '123'):
            usuario = User(1, name, password)
            login_user(usuario)
            return redirect(url_for('protected'))
    return render_template('login.html', form = form)




@app.route('/protected/')
@login_required
def protected():
    return "home: <a href='/login/'>Login</a> <a href='/protected/'>Protected</a> <a href='/logout/'>Logout</a>"

@app.route('/login/')
def login():
    login_user(User(1))
    return "you are logged in"

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=1212,debug=True)

