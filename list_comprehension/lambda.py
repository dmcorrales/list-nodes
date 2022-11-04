from functools import reduce


def example_1():
    x = lambda a :  a + 10
    print(x(5))

def example_2():
    x = lambda a,b :  a + b
    print(x(5,1))

def example_3():
    x = lambda result, result2 : True if result > 2 or result2 > 3 else False
    print(x(3,2))

def example_4():
    x = map(lambda x,y : {x:y},['a','b','c'], ['d','e','f'])
    print(list(x))

def example_5():
    x = list(filter(lambda y : y > 1,range(3)))
    print(x)

def example_6():
    x = reduce(lambda w,y : w+y , [1,2,4])
    print(x)

def example_7():
    running = lambda km: "Success" if km >= 8 else "DIE"
    print(running(8))

def int_func(value):
        return value * 2

def example_8():

    x = list(map(int_func, [1,2,3]))
    print(x)

def example_9():
    x = reduce(lambda x,y : x + y , [1,2,3])
    print(x)

if __name__ == '__main__':
    example_9()