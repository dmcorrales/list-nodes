def locate_card(cards, query):
    pass

"""

arr = 1,2,3,4,5,6

1. 
low = 0   
high = 5
x = 4
mid = 2

mid > 4 ? NO
mid < 4 ? YES

2. 
low = 3
high = 5
x = 4

mid =  4
return 4

----------------------

1.
low = 0
high = 5
x = 1
mid = 2

mid > x ? True

2.
low = 0
high = 1
mid = 0

return 1

"""
def binary_search(array ,min, max, x):

    mid = (min + max) // 2

    if array[mid] == x:
        return x

    if array[mid] > x:
        return binary_search(array, min, mid - 1, x)
    else:
        return binary_search(array, mid + 1 , max, x)


if __name__ == '__main__':
    w = [1,2,3,4,5,6]
    print(binary_search(w, 0, len(w)-1, 4))