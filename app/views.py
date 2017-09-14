from app import app,lm
from flask import render_template,redirect,url_for,request,session,g,jsonify
#from .forms import LoginForm
from flask_login import login_required,login_user,logout_user,current_user
from .models import User,Sys_info
from .info import info,appinfo
from .user import userlogin
from .ansibleapi import ansibleapi

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

app.register_blueprint(userlogin.user)
app.register_blueprint(info.info)
app.register_blueprint(appinfo.appinfo)
app.register_blueprint(ansibleapi.ansibleapi)


@app.route("/test1")
def test1():
	return render_template("test1.html")


@app.route("/test2")
def test2():
	return render_template("test2.html")


@app.route("/home")
def home():
	return render_template("home.html")

@app.route('/api/tasks')
def gettasks():
	tasks = [
            {
			'id': 1,
			'title': u'Buy groceries',
			'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
			'done': False
			},
            {
			'id': 2,
			'title': u'Learn Python',
			'description': u'Need to find a good Python tutorial on the web',
			'done': False
            }
	]
	return jsonify({"task":tasks})
