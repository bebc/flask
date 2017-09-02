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
		infodic = {'ip':info.ip,'sys':info.sys,'application':info.application}
		infolist.append(infodic)
	#return jsonify({"total":syscount,"infolist":infolist}) 服务端分页返回格式
	return jsonify(infolist)

@info.route("/api/addinfo",methods = ['GET','POST'])
def sysadd():

	if request.method == 'POST':
		addip = request.form.get('addip')
		addsys = request.form.get('addsys')
		addusage = request.form.get('addusage')
		checkip = models.Sys_info.query.filter_by(ip=addip).first()

		if checkip == None:
			addinfo = models.Sys_info(ip=addip,sys=addsys,application=addusage)
			checkdbadd = db.session.add(addinfo)
			if checkdbadd == None:
				checkdbcommit = db.session.commit()
			if checkdbcommit == None:
				return "addsuccess"
		else:
			return "addfail"

	return "/api/addinfo"

@info.route("/api/delinfo",methods = ['GET','POST'])
def sysdel():

	if request.method == 'POST':
		getdata = request.get_data()
		jsondata = json.loads(getdata)

		for data in jsondata:
			try:
				deldata = models.Sys_info.query.filter_by(ip=data["ip"],sys=data["sys"],application=data["application"]).first()
				db.session.delete(deldata)
				db.session.commit()
				#return "delsuccess"
			except:
				return "delfail"

		return "delsuccess"
