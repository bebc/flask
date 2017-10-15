from app import app
from app import socketio,db
from flask_socketio import SocketIO,emit,disconnect
from app.models import Deploy_info,Application_info
from flask_uploads import UploadSet, configure_uploads, ALL
from flask import request,jsonify,session
from flask import Blueprint
from flask import session
from app.deploy.deploy_cmd import *
from app.public.base import *
from datetime import datetime

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
        name = session['username']
        #定义文件名全局变量后续websocket读取文件会调用
        global logfile
        logfile = '/data/logs/flask/'+web_project+'-'+deploy_version+'.log'
        #信息入库
        try:
            deploy_info = Deploy_info(name=name,webproject=web_project,version=deploy_version,log_file=logfile,result=201)
            db.session.add(deploy_info)
            db.session.commit()
        except Exception as e:
            return e

        log.record_log()
        for app in web_server:
            server = Application_info.query.filter_by(webserver=app).first()
            ip.append(server.ip)
        #运行任务
        result = run_thread(ip,web_project,deploy_version)
        log.remove_handler()

        #更新入库信息和结果
        try:
            update_info = Deploy_info.query.filter_by(webproject=web_project,version=deploy_version).first()
            update_info.result = 200
            update_info.execute_date = datetime.now()
            db.session.commit()
        except Exception as e:
            return e

        return jsonify({"code": 200, "msg": "请等待..."})

@socketio.on('my event',namespace='/msg')
def return_deploy_log(message):
    #测试代码
    #emit('connect', {'log': 10, 'message': message['data']})
    f = open(logfile)
    num = 0
    while (num < 15):
        data = f.readlines()
        for log in data:
            emit('connect',{'log':log,'message':message['data']})
        num += 1
        print (num)

    disconnect()




