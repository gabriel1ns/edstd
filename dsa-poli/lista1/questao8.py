class Node:
    def __init__(self, pagina):
        self.pagina = pagina 
        self.next = None
        self.previous = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def insert(self, pagina):
        new_node = Node(pagina)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove(self):
        
        if self.isEmpty():
            return None
        
        rempage = self.tail.pagina
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
            
        return rempage
        


class Sim:
    
    def __init__(self):
        self.historico = Deque()
        self.pilha_avancar = [] 

    def acessar_pagina(self, pagina):
        
        self.historico.insert(pagina)
        self.pilha_avancar.clear()

    def voltar(self):
        lastpag = self.historico.remove()
        
        if lastpag:
            self.pilha_avancar.append(lastpag)
            
    def avancar(self):
        
        if not self.pilha_avancar:
        
            return
        
        nextpag = self.pilha_avancar.pop()
        self.historico.insert(nextpag)

