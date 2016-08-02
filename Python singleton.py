"""A non thread safe implementation of singleton in Python using metaclass.

    It can be pictured as:
        MyClass = __metaclass__()
        MyObject = MyClass()

    So all object instances are created by the call method of the metaclass.
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print "__call__ gets called"
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    def __new__(cls, clsname, bases, dct):
        print "__new__ gets callled"
        return super(Singleton, cls).__new__(cls, clsname, bases, dct)


class MyClass(object):
    __metaclass__ = Singleton


a = MyClass()
b = MyClass()
assert a is b
