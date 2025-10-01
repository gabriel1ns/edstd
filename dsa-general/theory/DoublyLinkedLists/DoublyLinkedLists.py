class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedLists:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.length +=1

        return True
    
    def pop(self):
        if self.length == 0:
            return None

    
        temp = self.tail
    
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
            temp.previous = None
    
        self.length -= 1
        return temp.value
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

        self.length +=1
        return True
    
    def pop_first(self):
        
        if self.length == 0:
            return None
        
        temp = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
            temp.next = None

        self.length -= 1;
        return temp.value
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        if index < self.length /2 :
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index , -1):
                temp = temp.previous
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.prepend(value)
        if index == self.length:
            self.append(value)

        new_node = Node(value)
        before = self.get(index-1)
        after = before.next

        new_node.previous = before
        new_node.next = after
        before.next = new_node
        after.previous = new_node

        self.length += 1
        return True

    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        
        temp = self.get(index)
        temp.next.previous = temp.previous
        temp.previous.next = temp.next
        temp.next = None
        temp.previous = None

        self.length -= 1
        return temp

my_linked_list = DoublyLinkedLists(1)
my_linked_list.append(2)
my_linked_list.prepend(3)
my_linked_list.set_value(0,5)
my_linked_list.insert(1,4)

my_linked_list.printList()
my_linked_list.remove(2)
my_linked_list.printList()


