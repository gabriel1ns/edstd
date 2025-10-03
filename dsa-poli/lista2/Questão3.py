from collections import deque

class FilaCircular:
    def __init__(self, tamanho_max):
        if tamanho_max <= 0:
            raise ValueError("O tamanho deve ser um valor positivo")
        
        self.fila = deque(maxlen = tamanho_max)
        self.tamanho_max = tamanho_max

    def enfileirar(self, elemento):
        self.fila.append(elemento)

    def desenfileirar(self):
        
        if not self.fila:
            raise ValueError("A fila está vazia")
        
        elemento_removido = self.fila.popleft()
        return elemento_removido

    def exibir(self):
        print(f"Tamanho da Fila: (Tamanho {len(self.fila)}/{self.tamanho_max}): {list(self.fila)}")