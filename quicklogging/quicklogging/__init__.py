'''logging configuration package with more addition functions

available interface:
@Quicklogging()
set_logger()
get_logger()
'''

__version__ = '1.0'

from ._quick_logging import *
get_logger = QuickLogging.get_logger
set_logger = QuickLogging.set_logger