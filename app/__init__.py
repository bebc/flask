from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate,MigrateCommand
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

from app import views,models
#import pymysql
#pymysql.install_as_MySQLdb()


