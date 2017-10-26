1.本程序基于python3开发,实现一个包括主机资产管理，应用发布的运维平台，并且集成了ansible模块以及使用celery实现异步的定时任务

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

4.启动程序

python3 run.py
