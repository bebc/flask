from app import app
from app.models import Application_info
from flask_uploads import UploadSet, configure_uploads, ALL
from flask import request,jsonify,session
from flask import Blueprint
from app.deploy.deploy_cmd import *
from app.public.base import *

deploy_add = Blueprint('deploy_add',__name__)

files = UploadSet('files', ALL)
configure_uploads(app, files)

@deploy_add.route("/upload_file",methods = ['GET','POST'])
def upload_file():
    if request.method == 'POST' and 'war' in request.files:
        filename = files.save(request.files['war'])
        app.logger.info(filename)
        url = files.url(filename)
    return "upload_file"


@deploy_add.route("/deploy/deploy_app",methods = ['GET','POST'])
def deploy_app():
    ip = []
    if request.method == 'POST':
        web_project = request.form.get('web_project')
        deploy_version = request.form.get('deploy_version')
        web_server = request.form.getlist('web_server')
        record_log(web_project+'-'+deploy_version+'.log')
        for app in web_server:
            server = Application_info.query.filter_by(webserver=app).first()
            ip.append(server.ip)
        result = run_thread(ip)

        return jsonify({"code": 200, "msg": result})



