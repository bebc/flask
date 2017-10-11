from app import db
from app.models import Ops_record
from flask import session


class OpsRecord:
    def __init__(self):
        pass

    def asset_record(self,ops_type,service_type):
        name = session['username']
        try:
            data = Ops_record(name=name,ops_type=ops_type,service_type=service_type)
            db.session.add(data)
            db.session.commit()
        except Exception as e:
            return e




