class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho

    def push(self, elemento):
        novo_no = No(elemento)
        
        novo_no.proximo = self.topo
        self.topo = novo_no

        self.tamanho += 1

    def pop(self):
        if self.tamanho == 0:
            raise ValueError("A Pilha está vazia")
            
        elemento_removido = self.topo.dado
        
        self.topo = self.topo.proximo

        self.tamanho -= 1

        return elemento_removido
    
    def espiar(self):
        if self.tamanho == 0:
            raise ValueError("A Pilha está vazia")
        
        return self.topo.dado
    
    def inverter_pilha(self):

        if len(self) <= 1:
            return self
        
        pilha_invertida = Pilha()

        while self.tamanho > 0:
            pilha_invertida.push(self.pop())

        self.topo = pilha_invertida.topo
        self.tamanho = pilha_invertida.tamanho

        return self