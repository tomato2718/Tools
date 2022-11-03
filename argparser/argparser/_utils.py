'''utils used by argparser
'''

__all__ = ['get_version']

from inspect import stack

# bugged
def get_version():
    '''get main program's version
    -return<str>: main program's version
    '''
    try:
        version =  stack()[3][0].f_locals['__version__']
    except:
        version = ''
    return version