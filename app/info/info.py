import json
from app import models,db
from flask import request,jsonify
from flask import Blueprint

info = Blueprint('info',__name__)

@info.route("/api/info")
def sysinfo():
	sysinfo = models.Sys_info.query.all()
	'''
	服务端分页代码
	pagelimit = int(request.args.get('limit'))
	pageoffset = int(request.args.get('offset'))+1
	sysinfo = Sys_info.query.paginate(pageoffset,pagelimit,False).items
	syscount = Sys_info.query.count()
	'''
	infolist = []

	for info in sysinfo:
		infodic = {'id':info.id,'ip':info.ip,'sys':info.sys,'application':info.application,'webserver':info.webserver}
		infolist.append(infodic)
	#return jsonify({"total":syscount,"infolist":infolist}) 服务端分页返回格式
	return jsonify(infolist)

@info.route("/api/addinfo",methods = ['GET','POST'])
def sysadd():
	if request.method == 'POST':
		addip = request.form.get('addip')
		addsys = request.form.get('addsys')
		addapplication = request.form.get('addapplication')
		addwebserver = request.form.get('addwebserver')
		addwebproject = request.form.get('addwebproject')
		checkip = models.Sys_info.query.filter_by(ip=addip).first()

		if checkip == None and addapplication == 'tomcat' and addwebserver != None and addwebproject != None:
			try:
				addinfo = models.Sys_info(ip=addip,sys=addsys,application=addapplication,webserver=addwebserver)
				addapplicationinfo = models.Application_info(ip=addip,webserver=addwebserver,webproject=addwebproject)
				db.session.add(addinfo)
				db.session.add(addapplicationinfo)
				db.session.commit()
				return "addsuccess"
			except:
				return "fail"
		elif checkip == None:
			try:
				addinfo = models.Sys_info(ip=addip,sys=addsys,application=addapplication,webserver=addwebserver)
				db.session.add(addinfo)
				db.session.commit()
				return "addsuccess"
			except:
				return "fail"
		else:
			return "addfail"

	return "/api/addinfo"

@info.route("/api/delinfo",methods = ['GET','POST'])
def sysdel():
	if request.method == 'POST':
		getdata = request.get_data()
		jsondata = json.loads(getdata)

		for data in jsondata:
			if data["application"] == 'tomcat':
				try:
					deldata = models.Sys_info.query.filter_by(id=data["id"],ip=data["ip"],sys=data["sys"],application=data["application"],webserver=data["webserver"]).first()
					db.session.delete(deldata)
					models.Application_info.query.filter_by(ip=data["ip"],webserver=data["webserver"]).delete()
					db.session.commit()
				except:
					return "delfail"
			else:
				try:
					deldata = models.Sys_info.query.filter_by(id=data["id"],ip=data["ip"],sys=data["sys"],application=data["application"],webserver=data["webserver"]).first()
					db.session.delete(deldata)
					db.session.commit()
				except:
					return "delfail"

		return "delsuccess"

@info.route("/api/updateinfo",methods = ['GET','POST'])
def sysupdate():
	if request.method == 'POST':
		updateid = request.form.get('updateid')
		updateip = request.form.get('updateip')
		updatesys = request.form.get('updatesys')
		updateapplication = request.form.get('updateapplication')
		updateinfo = models.Sys_info.query.filter_by(id=updateid).first()
		
		if updateinfo != None:
			try:
				updateinfo.ip = updateip
				updateinfo.sys = updatesys
				updateinfo.application = updateapplication
				db.session.commit()
				return "updatesuccess"
			except:
				return "updatefail"
		else:
			return "updatefail"

	return "/api/updateinfo"
