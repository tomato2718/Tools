import logging, logging.config
import os
from sys import argv

import yaml

from ._constants import *

class QuickLogging():
    def __init__(self, path_ = PATH):
        self.path = path_
    
    # decorator call
    def __call__(self, func):
        from functools import wraps
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                config_ = self.__readConfig(self.path)
                logging.config.dictConfig(config_)
            except Exception as e:
                logging.error(e)
                os._exit(0)
            func(*args, **kwargs)
        return wrapper

    # function call
    @classmethod
    def quick_logging(cls, path_ = PATH):
        try:
            config_ = cls.__readConfig(path_)
            logging.config.dictConfig(config_)
        except Exception as e:
            logging.error(e)
            os._exit(0)

    @classmethod
    def __readConfig(cls, path_):
        path_ = os.path.join(os.path.dirname(argv[0]), path_)
        with open(path_) as file:
            config = yaml.safe_load(file)
        return config