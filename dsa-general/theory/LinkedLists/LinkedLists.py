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
        
    def pop(self):

        if self.lenght == 0:
            return None
        
        temp = self.head
        pre = self.head

        while(temp.next):
            pre = temp
            temp = temp.next #moving temp over
        self.tail = pre
        self.tail.next = None
        self.lenght -= 1

        if self.lenght == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self,value):
        new_node = Node(value)

        if self.lenght == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head #we want new_node to point to head, to after change it to the head completely
            self.head = new_node
        self.lenght += 1
        return True
    
    def pop_first(self):
        if self.lenght == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.lenght -=1

        if self.lenght == 0:
            self.tail = None
        return temp
    
    def get(self,index):
        if index < 0 or index >= self.lenght:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        return False


my_linked_list = LinkedList(11)
my_linked_list.append(90)
my_linked_list.append(45)
my_linked_list.append(21)

my_linked_list.printList()

my_linked_list.set_value(2,56)
my_linked_list.printList()