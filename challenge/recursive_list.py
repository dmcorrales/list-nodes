import random


class Node:

    def __init__(self):
        self.next = None

    @property
    def random(self):
        return random.random()

    def add(self):
        if not self.next:
            self.next = Node()
        else:
            self.next.add()


def print_nodes(list_elements):
    if list_elements:
        print(list_elements.random)
        print_nodes(list_elements.next)

def print_reverse_nodes(list_elements):
    if list_elements:
        print_reverse_nodes(list_elements.next)
        print(list_elements.random)

if __name__ == '__main__':
    list = Node()
    list.add()
    list.add()
    print_reverse_nodes(list)
    print_nodes(list)


