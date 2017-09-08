import json
from app.ansibleapi.localapi import *
from app import models,db
from flask import request,jsonify
from flask import Blueprint

ansibleapi = Blueprint('ansibleapi',__name__)

@ansibleapi.route("/ansibleapi/detailinfo",methods = ['GET','POST'])
def detailinfo():
	try:
		getip = request.args.get('ip')
		information = infodetail("/etc/ansible/hosts",getip,"setup","")
		return jsonify(information)
	except:
		return "fail"

