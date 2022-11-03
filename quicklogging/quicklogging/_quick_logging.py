'''logging configuration package with more addition functions

available interface:
@Quicklogging()
set_logger()
get_logger()
'''

__all__ = ['QuickLogging']

import logging, logging.config

import yaml

from ._utils import *
from ._constants import *

class QuickLogging():
    def __init__(self, path=PATH):
        '''Configure logging from yaml file, same as set_logger()
        path<str>: your logging config path, default = "conf/logging_config.yml"
        '''
        self.path_ = path
    
    def __call__(self, func):
        from functools import wraps
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.set_logger(self.path_)
            func(*args, **kwargs)
        return wrapper

    @classmethod
    def set_logger(cls, path: str = PATH) -> None:
        '''Configure logging from yaml file
        path<str>: your logging config path, default = "conf/logging_config.yml"
        '''
        config_ = cls.__read_config(path)
        config_ = set_abs_path(config_, 'filename')
        logging.config.dictConfig(config_)
    
    @staticmethod
    def get_logger(target: str) -> logging.Logger:
        '''Literal logging.getlogger()
        - target<str>: the logger you want to get
        - return<logging.Logger>: return the requested logger
        '''
        return logging.getLogger(target)

    @classmethod
    def __read_config(cls, path_) -> dict:
        '''Read config from yaml file
        - return<dict>: the result got after parsing yaml file
        '''
        path_ = get_abs_path(path_)
        with open(path_, 'r') as file:
            config = yaml.safe_load(file)
        return config