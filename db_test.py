#!flask/bin/python

#from migrate.versioning import api
from app import db,models

u = models.User(name='john',password='123')
#user = models.User.query.first()
#user.password='123'
db.session.add(u)
db.session.commit()
