from collections import deque

class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None 
        self._tamanho = 0 
    
    def push(self, elemento): 
        novo_no = No(elemento) 
        novo_no.proximo = self.topo 
        self.topo = novo_no
        self._tamanho += 1 
    
    def pop(self): 
        if self._tamanho > 0:
            no_removido = self.topo 
            self.topo = self.topo.proximo
            self._tamanho -= 1
            return no_removido.dado 
        else:
            raise IndexError("A Pilha está vazia")

    def espiar(self): 
        if self.topo is None:
            raise ValueError("A Pilha está vazia")
        else: 
            return self.topo.dado
    
    def __repr__(self):
        r = ""
        ponteiro = self.topo
        while ponteiro is not None:
            r = r + str(ponteiro.dado) + "\n"
            ponteiro = ponteiro.proximo
        return r
    
    def __str__(self): 
        return self.__repr__()
    
class PilhaDeque:
    def __init__(self):
        self._dados = deque()

    def push(self, elemento):
        self._dados.append(elemento)

    def pop(self):
        if len(self._dados) > 0:
            return self._dados.pop()
        else:
            raise IndexError("A Pilha está vazia")

    def espiar(self):
        if len(self._dados) > 0:
            return self._dados[-1]
        else:
            raise IndexError("Não é possível espiar Pilha vazia")
    
    def __str__(self):
        return f"PilhaDeque({list(self._dados)})"

