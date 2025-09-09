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


    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node #we need that what comes after the last item (tail) to stop pointing to None and point to new_node
            self.tail = new_node
        self.lenght += 1
        return True #For future reference.
        

my_linked_list = LinkedList(1);
my_linked_list.printList()


my_linked_list.append(2)
my_linked_list.printList()

