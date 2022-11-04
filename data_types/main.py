def str_data_type():
    x = "Hello WORLD"
    print(x)
    print(x[0])
    print(x[0:5])
    print(x[::-1])
    print(x[::3])
    print(x * 2)

def set_data_type():
    x = "HOLA PAPITO!!"
    s = set(x)
    s.add("X")
    print(s)

def frozenset_data_type():
    x = frozenset("dracula")
    print(x)

def dict_data_type():
    dict = {"a": 1, "b": 2}
    print(dict.items())
    print(dict.keys())
    print(dict.values())

def tuple_data_type():
    tuple_1 = (1,2,3)
    x = [1,2,3]
    x.remove(2)
    print(x)

def dict_super_set():
    x = {1,2,3,4,5,1,1,1,1}
    x.add(6)
    x.discard(4)
    x.remove(1)
    x.update({4,6})
    y = {frozenset(x), frozenset({2,3,45})}
    print(y)

    from collections import Counter
    print(Counter(x))

def incrementer():
    actual_val = 0
    def sum():
        nonlocal actual_val
        actual_val += 1
        return actual_val
    return sum

wx = "HOLA"
def global_get():
    global wx
    X = "B"
    del X

def testing():
    d = {"key": "value"}
    d = {**d, **{"value": "value"}}
    print(d)

def _my_gen():
    while True:
        yield 0


if __name__ == '__main__':
    incremen = incrementer()()
    testing()
    my_gen = _my_gen()
    print(repr(my_gen))
    print(my_gen.__next__())
    print(my_gen.__next__())
