from multiprocessing import Pool

def example_1(x):
    return x ** 3

if __name__ == '__main__':
    pool = Pool(5)
    result = pool.map(example_1, [1, 2, 3])
    print(result)

import multiprocessing
def countdown(count):
 while count > 0:
 print("Count value", count)
 count -= 1
 return
if __name__ == "__main__":
 p1 = multiprocessing.Process(target=countdown, args=(10,))
 p1.start()
 p2 = multiprocessing.Process(target=countdown, args=(20,))
 p2.start()
 p1.join()
 p2.join()