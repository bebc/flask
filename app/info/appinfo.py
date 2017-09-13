import json
from app import db
from app.models import Application_info
from flask import request,jsonify
from flask import Blueprint

appinfo = Blueprint('appinfo',__name__)

@appinfo.route("/api/appinfo",methods = ['GET','POST'])
def Appinfo():
	getwebproject = str(request.args.get('webproject'))
	if getwebproject == 'null':
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

@appinfo.route("/api/appquery",methods = ['GET','POST'])
def appquery():
	if request.method == 'POST':
		getwebproject = str(request.get_data())
		webproject = Application_info.query.filter_by(webproject=getwebproject).all()
		#for data in webproject:
			
	return "appquery"

