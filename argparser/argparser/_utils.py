__all__ = ['get_version']

from inspect import stack

# bugged, may 
def get_version():
    try:
        version =  stack()[3][0].f_locals['__version__']
    except:
        version = ''
    return version