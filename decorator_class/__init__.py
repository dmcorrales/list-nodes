from types import MethodType


class MyDecorator():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("CALLING INTERNAL VALUES!!")
        return self.func(*args, **kwargs)

    def __get__(self, instance, cls):
        return self if instance is None else MethodType(self, instance)

@MyDecorator
def my_function():
    print("JELOO")

if __name__ == '__main__':
    my_function()
    import types
    print(type(my_function))