from app import app
from app import socketio
from flask_socketio import SocketIO,emit,disconnect
from app.models import Application_info
from flask_uploads import UploadSet, configure_uploads, ALL
from flask import request,jsonify,session
from flask import Blueprint
from app.deploy.deploy_cmd import *
from app.public.base import *
import time

deploy_add = Blueprint('deploy_add',__name__)

files = UploadSet('files', ALL)
configure_uploads(app, files)

@deploy_add.route("/upload_file",methods = ['GET','POST'])
def upload_file():
    log = Initlog('flaskupload.log')
    log.record_log()
    if request.method == 'POST' and 'war' in request.files:
        filename = files.save(request.files['war'])
        app.logger.info(filename)
        url = files.url(filename)
    log.remove_handler()
    return "upload_file"


@deploy_add.route("/deploy/deploy_app",methods = ['GET','POST'])
def deploy_app():
    ip = []
    if request.method == 'POST':
        web_project = request.form.get('web_project')
        deploy_version = request.form.get('deploy_version')
        web_server = request.form.getlist('web_server')
        log = Initlog(web_project+'-'+deploy_version+'.log')
        global logfile
        logfile = '/data/logs/flask/'+web_project+'-'+deploy_version+'.log'
        log.record_log()
        for app in web_server:
            server = Application_info.query.filter_by(webserver=app).first()
            ip.append(server.ip)
        #运行任务
        result = run_thread(ip,web_project,deploy_version)
        log.remove_handler()

        return jsonify({"code": 200, "msg": result})

@socketio.on('my event',namespace='/msg')
def test_socket(message):
    emit('connect', {'log': 10, 'message': message['data']})
    f = open(logfile)
    num = 0
    while (num < 15):
        data = f.readlines()
        for log in data:
            emit('connect',{'log':log,'message':message['data']})
        num += 1
        print (num)

    disconnect()




