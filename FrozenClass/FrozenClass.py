def FrozenClass(target):
    def __init__(self, *args, **kwargs):
        backup(self, *args, **kwargs)
        target.__is_freeze = True

    def __setattr__(self, key, value):
        if self.__is_freeze:
            raise Exception("could not add new attribute '%s' to '%s'"%(key,target.__name__))
        object.__setattr__(self, key, value)
    
    backup = target.__init__
    target.__is_freeze = False
    target.__init__ = __init__
    target.__setattr__ = __setattr__
    return target 
