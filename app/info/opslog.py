from app.models import Ops_record
from flask import request,jsonify,session
from flask import Blueprint

opslog = Blueprint('opslog',__name__)

@opslog.route("/api/opsinfo",methods = ['GET','POST'])
def record_info():
    opsinfo = Ops_record.query.all()
    opsinfolist = []

    for info in opsinfo:
        opsinfodic = {'id': info.id, 'name': info.name, 'ops_type': info.ops_type, 'service_type': info.service_type,
                   'date': info.date}
        opsinfolist.append(opsinfodic)

    return jsonify(opsinfolist)
