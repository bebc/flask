import json
from app.ansibleapi.localapi import *
from app import models,db
from flask import request,jsonify
from flask import Blueprint

ansibleapi = Blueprint('ansibleapi',__name__)

@ansibleapi.route("/ansibleapi/detailinfo",methods = ['GET','POST'])
def detail_info():
	try:
		getip = request.args.get('ip')
		information = infodetail("/etc/ansible/hosts",getip,"setup","")
		return jsonify(information)
	except:
		return "fail"

@ansibleapi.route("/ansibleapi/run_command",methods = ['GET','POST'])
def run_command():
	mod_type = request.form.get('mod_type')
	mod_param = request.form.get('mod_param')
	ip_addr = request.form.getlist('ip_addr')
	command = Ansible_hoc_api("/etc/ansible/hosts")
	for host in ip_addr:
		try:
			result = command.run_command(host, mod_type, mod_param)
			print (result)
			ip = list(result.keys())
			print (ip)
			for key in ip:
				print (result[key])
				if result[key]['changed'] == True:
					print (result[key]['stdout_lines'])
					return jsonify({"code":200,"msg":(result[key]['stdout_lines'])})
		except Exception as e:
			return jsonify({"code":400,"msg":str(e)})


