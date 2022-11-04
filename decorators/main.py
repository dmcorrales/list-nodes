import functools


def my_decorator(function):
    @functools.wraps(function)
    def x(x):
       func = function(x)
       if not isinstance(func, str):
           return "CANNOT GET RETURN"
       return func
    return x

def api_path(url=''):
    def decorate(funct):
        @functools.wraps(funct)
        def wrapper(*args, **kwargs):
            return funct(*args, **kwargs)
        return wrapper
    return decorate

@my_decorator
def hello_world(parameter):
    return parameter

@api_path(url="/")
def index(input):
    return "200"

if __name__ == '__main__':
    print(index({}))