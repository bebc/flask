#!flask/bin/python

from app import app
from app import socketio

#socketio.run(app,debug=True)
#app.run(host='0.0.0.0',debug = True)
if __name__ == '__main__':
	#app.wsgi_app = ProxyFix(app.wsgi_app)
	socketio.run(app,host='0.0.0.0',debug=True)
	#app.run(host='0.0.0.0',debug = True,threaded=True)

