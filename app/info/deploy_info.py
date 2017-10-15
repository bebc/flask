from app.models import Deploy_info
from flask import request,jsonify,session
from flask import Blueprint

deploy_info = Blueprint('deploy_info',__name__)

@deploy_info.route("/api/deploy_info",methods = ['GET','POST'])
def get_data():
    info_data = Deploy_info.query.all()
    info_list = []

    for info in info_data:
        infodic = {'id': info.id, 'name': info.name, 'web_project': info.webproject, 'version': info.version,
                   'result': info.result, 'create_date': info.create_date, 'execute_date': info.execute_date}
        info_list.append(infodic)

    return jsonify(info_list)
