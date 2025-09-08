class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)

        #poiting start and finish of the list to the new node
        self.head = new_node
        self.tail = new_node
        self.lenght = 1

my_ll = LinkedList(4);
print(my_ll.head.value)