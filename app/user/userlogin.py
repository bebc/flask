from app import app,lm
from flask import render_template,redirect,url_for,request,session,g,jsonify
from flask_login import login_required,login_user,logout_user,current_user
from app import models
from flask import Blueprint

user = Blueprint('user',__name__)

@lm.user_loader
def load_user(id):
	return models.User.query.get(id)

@app.before_request
def before_request():
	g.user = current_user

@user.route('/login',methods = ['GET','POST'])
def login():
    #if g.user is not None and g.user.is_authenticated:
       # return redirect(url_for('index'))

	if request.method == 'POST':
		user = models.User.query.filter_by(name=request.form.get('username')).first()
		#name=request.form.get('username')
		password = request.form.get('password', None)
		#user = User(name, password)
		if user is not None and user.is_active and user.confirm_password(password):
			login_user(user)
			return user.name

		else:
			return "not active"

	#loginform = LoginForm()
	return render_template("login.html")

@user.route("/logout")
def logout():
	logout_user()
	return	render_template("index.html")


