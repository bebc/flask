import json
from app import db
from app.models import Application_info
from flask import request,jsonify
from flask import Blueprint

appinfo = Blueprint('appinfo',__name__)

@appinfo.route("/api/appinfo",methods = ['GET','POST'])
def Appinfo():
	getwebproject = str(request.args.get('webproject'))
	if getwebproject == 'null' or getwebproject == 'All':
		appinfo = Application_info.query.all()
		'''
		服务端分页代码
		pagelimit = int(request.args.get('limit'))
		pageoffset = int(request.args.get('offset'))+1
		sysinfo = Sys_info.query.paginate(pageoffset,pagelimit,False).items
		syscount = Sys_info.query.count()
		'''
		infolist = []

		for info in appinfo:
			infodic = {'id':info.id,'ip':info.ip,'webserver':info.webserver,'webproject':info.webproject}
			infolist.append(infodic)
		#return jsonify({"total":syscount,"infolist":infolist}) 服务端分页返回格式
		return jsonify(infolist)

	else:
		appinfo = Application_info.query.filter_by(webproject=getwebproject).all()
		infolist = []

		for info in appinfo:
			infodic = {'id':info.id,'ip':info.ip,'webserver':info.webserver,'webproject':info.webproject}
			infolist.append(infodic)
        #return jsonify({"total":syscount,"infolist":infolist}) 服务端分页返回格式
		return jsonify(infolist)


@appinfo.route("/api/appselect",methods = ['GET','POST'])
def appselect():
	appdatalist=[]
	try:
		appselect = Application_info.query.with_entities(Application_info.webproject).distinct().all()
		for appdata in appselect:
			appdatalist.append(str(appdata)[2:-3])
		return jsonify(appdatalist)
	except:
		return "fail"

@appinfo.route("/api/appadd",methods = ['GET','POST'])
def appquery():
	if request.method == 'POST':
		addappproject = request.form.get('addappproject')	
		addip = request.form.get('addip')	
		addappwebserver = request.form.get('addappwebserver')	
		checkapp = Application_info.query.filter_by(ip=addip,webserver=addappwebserver,webproject=addappproject).first()
		if checkapp == None:
			try:
				addappinfo = Application_info(ip=addip,webproject=addappproject,webserver=addappwebserver)
				db.session.add(addappinfo)
				db.session.commit()
				return "appaddsuccess"
			except:
				return "appaddfail"
		else:
			return "appexist"

@appinfo.route("/api/appdel",methods = ['GET','POST'])
def appdel():
	if request.method == 'POST':
		getdata = request.get_data()
		jsondata = json.loads(getdata)

		for data in jsondata:
			try:
				delapp = Application_info.query.filter_by(ip=data["ip"],webproject=data["webproject"],webserver=data["webserver"]).first()
				db.session.delete(delapp)
				db.session.commit()
			except:
				return "delfail"
		
		return "delsuccess"
