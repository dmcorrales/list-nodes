def example_1():
    x = [i for i in range(10)]
    return x

def example_2():
    x = [i for i in range(10) if i == 9]
    return x

def example_3():
    hot_temps = [qw for _ in range(20) if (qw := 10) >= 100]
    return x

def example_4():
    x = [(x,y) for x in [1,2,3] for y in [3,4,5]]
    return x

def example_5():
    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)

if __name__ == '__main__':
    to_print = [example_5()]
    for x in to_print:
        print(x)
