
def test():
    x = 0
    while True:
        x+=1
        yield x

def test_2():
    yield from range(10)

if __name__ == '__main__':
    for x in test():
        if x < 7:
            print(x)
    print(list(test_2()))

