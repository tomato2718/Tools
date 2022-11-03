'''utils used by quicklogging
'''

__all__ = ['get_abs_path', 'set_abs_path']

from sys import argv
import os

def get_abs_path(path_: str) -> str:
    '''Get absolute path of relative path
    - path_<str>: relative path
    - return<str>: absolute path of input
    '''
    return os.path.join(os.path.dirname(argv[0]), path_)


def set_abs_path(dic: dict, target: str) -> dict:
    '''Convert all relative path in dict to absolute
    - dic<dict>: target dict
    - target<str>: target key
    - return<dict>: converted dict
    '''
    for k, v in dic.items():
        if isinstance(v, dict):
            dic[k] = set_abs_path(v, target)
        elif k == target:
            dic[k] = get_abs_path(v)
    return dic

