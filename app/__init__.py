from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager, Shell

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app,db)
#manager = Manager(app)
#manager.add_command('db',MigrateCommand)
lm = LoginManager()
lm.init_app(app)

from app import views,models
#import pymysql
#pymysql.install_as_MySQLdb()


