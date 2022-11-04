class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

def print_all_values(root):
    if root:
        print(root.data)
        next_element = root.next
        while next_element:
            print(next_element.data)
            next_element = next_element.next

def print_reverse_values(root):
    """This function prints reverse values!"""
    result_element = []
    if root:
        result_element.append(root.data)
        next_element = root.next
        while next_element:
            result_element.append(next_element.data)
            next_element = next_element.next
    print(result_element[::-1])

def lamda_factorial():
     y = lambda x : 1 if x == 0 else x * y(x-1)
     print(y(4))

def x_y(*args, **kwargs):
    print(args, kwargs)

if __name__ == '__main__':
    lamda_factorial()
    import sys
    print(sys.getrecursionlimit())
    x_y(1,2,3, a=1, b=2, c=3)



