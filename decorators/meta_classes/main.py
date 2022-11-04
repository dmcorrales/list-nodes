from abc import ABC
from functools import wraps, partial

def debug(func=None, *, prefix=''):
    if func is None:
        return partial(debug, prefix=prefix)
    msg = prefix + func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper

def debugmethods(cls):
    print(vars(cls).items())
    for name, val in vars(cls).items():
        if callable(val):
            setattr(cls, name, debug(val))
            return cls

class MyMetaClass(type):

    def __new__(cls, clsname, bases, clsdict):
        print(clsname)
        print(bases)
        print(clsdict)
        clsobj = super().__new__(cls, clsname,
                                 bases, clsdict)
        print(clsobj)
        clsobj = debugmethods(clsobj)
        print(clsobj)
        return clsobj

class Base(metaclass=MyMetaClass):
    def __init__(self, my_base):
        self.x = 0

    def over(self):
        return "OK"

if __name__ == '__main__':
    Base("123")