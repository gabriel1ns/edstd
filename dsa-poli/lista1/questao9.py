class Thing:
    def __init__(self,nome, prioridade):
        self.nome = nome;
        self.prioridade = prioridade
        self.next = None

class Queue:
    def __init__(self):
        self.start = None
    
    def isEmpty(self):
        return self.start is None

    def enqueue(self, nome, prioridade):
        new_node = Thing(nome, prioridade)

        if self.isEmpty() or new_node.prioridade > self.start.prioridade:
            new_node.next = self.start
            self.start = new_node
            return
        
        current = self.start
        while current.next is not None and new_node.prioridade < current.next.prioridade:
            current = current.next
        
        new_node.next = current.next
        current.next = new_node

    def dequeue(self):
        if self.isEmpty():
            return None
        
        thing_deq = self.start
        self.start = self.start.next

        return thing_deq
