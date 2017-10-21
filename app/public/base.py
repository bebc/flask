from app import app
import logging

#日志类
class Initlog:

    def __init__(self,log_path):
        self.__handler = logging.FileHandler('/data/logs/flask/' + log_path, encoding='UTF-8')
        self.__handler.setLevel(logging.DEBUG)
        self.__logging_format = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s')
        self.__handler.setFormatter(self.__logging_format)

    def record_log(self):
        app.logger.addHandler(self.__handler)

    def remove_handler(self):
        app.logger.handlers.pop()
