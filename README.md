1.本程序基于python3开发

2.安装组件
pip3 install flask
pip3 install flask-login
pip3 install flask-sqlalchemy
pip3 install sqlalchemy-migrate
pip3 install flask-migrate
pip3 install flask-script
pip3 install mysqlclient
pip3 install celery
pip3 install celery-with-redis
pip3 install Flask-Uploads
pip3 install flask-socketio
pip3 install flower

3.初始化数据库
python3 db_create.py db init
python3 migrate.py db migrate
python3 migrate.py db upgrade

4.启动程序python3 run.py
