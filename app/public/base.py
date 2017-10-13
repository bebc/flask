from app import app
import logging

def record_log(log_path):
    handler = logging.FileHandler('/data/logs/flask/'+log_path, encoding='UTF-8')
    handler.setLevel(logging.DEBUG)
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
