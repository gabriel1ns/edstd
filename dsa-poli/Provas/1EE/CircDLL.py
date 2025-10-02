class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class CircularDLL:
    def __init__(self,value):
        new_node  = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            tail = self.head.previous
        tail.next = new_node
        new_node.previous = tail
        new_node.next = self.head
        self.head.previous = new_node

    def remove(self, value):
        if self.length == 0:
            return None
        
        temp = self.head
        for _ in range(self.length):
            if temp.value == value:
                if self.length == 1:
                    self.head = None
                    self.tail = None
                else:
                    
                    prev_node = temp.previous
                    next_node = temp.next
                    prev_node.next = next_node
                    next_node.previous = prev_node
                    
                    if temp == self.head:
                        self.head = next_node
                    
                    if temp == self.tail:
                        self.tail = prev_node
                
                self.length -= 1
                temp.next = None
                temp.previous = None
                return temp
            temp = temp.next
        return None
