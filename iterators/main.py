list1 = [ 25 , 78, 66, "rrr"]

a = iter(list1)
print(next(a))
print(next(a))
print(next(a))
print(next(a))


class MyIterator():

    def __iter__(self):
        self.val = 0
        return self

    def __next__(self):
        if self.val < 5:
            val = self.val
            self.val += 1
            return val
        else:
            raise StopIteration

if __name__ == '__main__':
    iter_f = iter(MyIterator())
    for x in iter_f:
        print(x)