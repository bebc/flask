from app import app,lm
from flask import render_template,redirect,url_for,request,session,g,jsonify
#from .forms import LoginForm
from flask_login import login_required,login_user,logout_user,current_user
from .models import User,Sys_info
from app.info import info,appinfo,opslog
from app.user import userlogin
from app.ansibleapi import ansibleapi
from app.deploy import deploy


app.register_blueprint(userlogin.user)
app.register_blueprint(info.info)
app.register_blueprint(appinfo.appinfo)
app.register_blueprint(ansibleapi.ansibleapi)
app.register_blueprint(opslog.opslog)
app.register_blueprint(deploy.deploy_add)


@app.route('/')
@app.route('/index')
@login_required
def index():
	return render_template("index.html")

@app.route("/test1")
@login_required
def test1():
	return render_template("test1.html")


@app.route("/test2")
@login_required
def test2():
	return render_template("test2.html")


@app.route("/opsinfo")
@login_required
def opsinfo():
	return render_template("opsinfo.html")

@app.route("/home")
@login_required
def home():
	return render_template("home.html")

@app.route("/deploy_add")
@login_required
def deploy_add():
	return render_template("/deploy/deploy_add.html")

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
