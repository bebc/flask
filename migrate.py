#!flask/bin/python

from app import app
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand


manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.run()
