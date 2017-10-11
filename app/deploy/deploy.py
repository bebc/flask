from app import app
from flask_uploads import UploadSet, configure_uploads, ALL
from flask import request,jsonify,session
from flask import Blueprint
from app.deploy.deploy_cmd import *

deploy_add = Blueprint('deploy_add',__name__)

files = UploadSet('files', ALL)
configure_uploads(app, files)

@deploy_add.route("/upload_file",methods = ['GET','POST'])
def upload_file():
    if request.method == 'POST' and 'war' in request.files:
        filename = files.save(request.files['war'])
        url = files.url(filename)
    return "upload_file"


@deploy_add.route("/deploy/deploy_app",methods = ['GET','POST'])
def deploy_app():
    if request.method == 'POST':
        web_project = request.form.get('web_project')
        deploy_version = request.form.get('deploy_version')
        web_server = request.form.getlist('web_server')
        result = run_thread(web_server)

        return jsonify({"code": 200, "msg": result})



