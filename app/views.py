from app import app,lm
from flask import render_template,redirect,url_for,request,session,g,jsonify
#from .forms import LoginForm
from flask_login import login_required,login_user,logout_user,current_user
from .models import User,Sys_info
from .info import info

@lm.user_loader
def load_user(id):
	return User.query.get(id)

@app.before_request
def before_request():
	g.user = current_user


@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/login',methods = ['GET','POST'])
def login():
    #if g.user is not None and g.user.is_authenticated:
       # return redirect(url_for('index'))

	if request.method == 'POST':
		user = User.query.filter_by(name=request.form.get('username')).first()
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

@app.route("/logout")
def logout():
	logout_user()
	return	render_template("index.html")

app.register_blueprint(info.info)

'''
@app.route("/api/info")
def sysinfo():
	sysinfo = Sys_info.query.all()
	服务端分页代码
	pagelimit = int(request.args.get('limit'))
	pageoffset = int(request.args.get('offset'))+1
	sysinfo = Sys_info.query.paginate(pageoffset,pagelimit,False).items
	syscount = Sys_info.query.count()
	infolist = []
	for info in sysinfo:
		infodic = {'id':info.id,'ip':info.ip,'sys':info.sys,'application':info.application}
		infolist.append(infodic)
	#return jsonify({"total":syscount,"infolist":infolist}) 服务端分页返回格式
	return jsonify(infolist)
'''

@app.route("/test1")
def test1():
	return render_template("test1.html")

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
