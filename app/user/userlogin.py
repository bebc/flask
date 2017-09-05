from app import app,lm
from flask import render_template,redirect,url_for,request,session,g,jsonify
from flask_login import login_required,login_user,logout_user,current_user
from app import models,db
from flask import Blueprint

user = Blueprint('user',__name__)

@lm.user_loader
def load_user(id):
	return models.User.query.get(id)

@app.before_request
def before_request():
	g.user = current_user

@user.route('/user/login',methods = ['GET','POST'])
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

@user.route("/user/logout")
def logout():
	logout_user()
	return	redirect(url_for('user.login'))

@user.route("/user/register",methods = ['GET','POST'])
def register():
	if request.method == "POST":
		username = request.form.get('user',None)
		password = request.form.get('passwd',None)
		email = request.form.get('email',None)
		department = request.form.get('department')
		user = models.User.query.filter_by(name=username).first()	
		if  user is not None and user.is_active:
			return "userexist"
		else:
			try:
				adduser = models.User(name=username,password=password,email=email,department=department)
				db.session.add(adduser)
				db.session.commit()
				return "success"
			except:
				return "fail"
	#return "success"








