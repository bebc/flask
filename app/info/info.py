from app import models
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
        infodic = {'id':info.id,'ip':info.ip,'sys':info.sys,'application':info.application}
        infolist.append(infodic)
    #return jsonify({"total":syscount,"infolist":infolist}) 服务端分页返回格式
    return jsonify(infolist)
