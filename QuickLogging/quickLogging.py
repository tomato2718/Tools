import logging, logging.config
import os, yaml
from functools import wraps


class QuickLogging():
    def __init__(self, path = "./Configs/logging_config.yml"):
        self.path = os.path.abspath(path)
        
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                self.__read_config()
                logging.config.dictConfig(self.config)
            except Exception as e:
                logging.error(e)
                os._exit(0)
            func(*args, **kwargs)
        return wrapper

    def __read_config(self):
        with open(self.path) as file:
            self.config = yaml.safe_load(file)

