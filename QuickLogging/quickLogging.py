import logging, logging.config
import os, sys, yaml
from functools import wraps


class QuickLogging():
    def __init__(self, path = "./Configs/logging_config.yml", getLoggers = ['main']):
        self.path = os.path.abspath(path)
        self.getLoggers = getLoggers
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                self.__read_config()
                logging.config.dictConfig(self.config)
                logger_dict = {}
                for _logger in self.getLoggers:
                    if _logger not in self.config['loggers']:
                        raise Exception('no logger %s found!'%_logger)
                    logger_dict[_logger] = logging.getLogger(_logger)

                kwargs['quickLogger'] = logger_dict
            except Exception as e:
                logging.error(e)
                os._exit(0)
            func(*args, **kwargs)
        return wrapper

    def __read_config(self):
        with open(self.path) as file:
            self.config = yaml.safe_load(file)

