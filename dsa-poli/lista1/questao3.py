class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Node:
    def __init__(self, pessoa):
        self.data = pessoa
        self.next = None

class CircularLL:
    def __init__(self):
        self.start = None
        
    
    def insert(self,pessoa):
        new_node = Node(pessoa)

        if self.start is None:
            self.start = new_node
            new_node.next = self.start
            return
        
        if new_node.data.idade < self.start.data.idade:
            current = self.start

            while current.next != self.start:
                current = current.next
            
            current.next = new_node
            new_node.next = self.start
            self.start = new_node

            return
    
        current = self.start

        while current.next != self.start and new_node.data.idade > current.next.data.idade:
            current = current.next
        
        new_node.next = current.next
        current.next = new_node