__all__ = ['QuickLogging']

import logging, logging.config

import yaml

from ._utils import *
from ._constants import *

class QuickLogging():
    def __init__(self, path=PATH):
        self.path_ = path
    
    # decorator call
    def __call__(self, func):
        from functools import wraps
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.set_logger(self.path_)
            func(*args, **kwargs)
        return wrapper

    # function call
    @classmethod
    def set_logger(cls, path = PATH) -> None:
        config_ = cls.__read_config(path)
        config_ = set_abs_path(config_, 'filename')
        logging.config.dictConfig(config_)
    
    @staticmethod
    def get_logger(target: str) -> logging.Logger:
        return logging.getLogger(target)

    @classmethod
    def __read_config(cls, path_) -> dict:
        path_ = get_abs_path(path_)
        with open(path_, 'r') as file:
            config = yaml.safe_load(file)
        return config