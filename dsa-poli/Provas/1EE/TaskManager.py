class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def  __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def peek(self):
        if self.height == 0:
            return None
        return self.value
    
    def push(self,value):
        new_node = node(value)

        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        