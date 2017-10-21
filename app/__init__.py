from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate,MigrateCommand
from flask_socketio import SocketIO
from celery import Celery,platforms
import logging
from flask_uploads import UploadSet, configure_uploads, ALL
#from flask_script import Manager, Shell

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app,db)
#manager = Manager(app)
#manager.add_command('db',MigrateCommand)
lm = LoginManager()
lm.login_view = "user.login"    #未登录返回页面配置项
lm.init_app(app)
socketio = SocketIO(app)
#celery = Celery(app.name,broker=app.config['CELERY_BROKER_URL'],backend=app.config['CELERY_RESULT_BACKEND'])
#celery.conf.update(app.config)
def make_celery(app):
    celery = Celery(app.name, backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    platforms.C_FORCE_ROOT = True
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

from app import views,models
#import pymysql
#pymysql.install_as_MySQLdb()


