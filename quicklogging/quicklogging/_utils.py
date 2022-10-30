__all__ = ['get_abs_path', 'set_abs_path']

from sys import argv
import os

def get_abs_path(path_: str) -> str:
    return os.path.join(os.path.dirname(argv[0]), path_)


def set_abs_path(dic: dict, target: str) -> dict:
    for k, v in dic.items():
        if isinstance(v, dict):
            dic[k] = set_abs_path(v, target)
        elif k == target:
            dic[k] = get_abs_path(v)
    return dic

