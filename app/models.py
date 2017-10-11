from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

class User(db.Model,UserMixin):
	id = db.Column(db.Integer,primary_key = True,autoincrement=True)
	name = db.Column(db.String(64),index = True,nullable=False)
	hash_password = db.Column(db.String(512),nullable=False)
	email = db.Column(db.String(120))
	department = db.Column(db.String(256))

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		try:
			return unicode(self.id)  # python 2
		except NameError:
			return str(self.id)  # python 3

	def __repr__(self):
		return '<User %r>' % (self.name)

	def __init__(self,name,password,email,department):
		self.name = name
		self.password = password
		self.email = email
		self.department = department

	@property
	def password(self):
		raise AttributeError('password cannot be read')

	@password.setter
	def password(self,password):
		self.hash_password=generate_password_hash(password)

	def confirm_password(self,password):
		return check_password_hash(self.hash_password,password)

class Sys_info(db.Model):
	id = db.Column(db.Integer,primary_key = True,autoincrement=True)
	ip = db.Column(db.String(64),index=True,nullable=False)
	sys = db.Column(db.String(512))
	application = db.Column(db.String(64))
	webserver = db.Column(db.String(64),index=True)

	def __repr__(self):
		return '<Ip %r>' % (self.ip)

class Application_info(db.Model):
	id = db.Column(db.Integer,primary_key = True,autoincrement=True)
	ip = db.Column(db.String(64),index=True,nullable=False)
	webserver = db.Column(db.String(64),nullable=False)
	webproject = db.Column(db.String(64),nullable=False)
	webpath = db.Column(db.String(128),nullable=False)
	webport = db.Column(db.String(64),nullable=False)

	def __reper_(self):
		return '<Ip %r>' % (self.ip)

class Ops_record(db.Model):
	id = db.Column(db.Integer,primary_key = True,autoincrement=True)
	name = db.Column(db.String(64),index = True,nullable=False)
	ops_type = db.Column(db.String(64),nullable=False)
	service_type = db.Column(db.String(64),nullable=False)
	date = db.Column(db.DateTime, default=datetime.now())

	def __reper_(self):
		return '<Name %r>' % (self.name)

class deploy_info(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(64), index=True, nullable=False)
	webproject = db.Column(db.String(64), nullable=False)
	version = db.Column(db.String(64), nullable=False)
	result = db.Column(db.String(64), nullable=False)
	create_date = db.Column(db.DateTime, default=datetime.now())
	execute_date = db.Column(db.DateTime, default=datetime.now())

	def __reper_(self):
		return '<Name %r>' % (self.name)





