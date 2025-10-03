class NoDuplo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

class Deck:
    def __init__(self):
        self._tamanho = 0
        self.cabeca = None
        self.cauda = None

    def __len__(self):
        return self._tamanho

    def inserir_frente(self, elemento):
        novo_no = NoDuplo(elemento)
        
        if self._tamanho == 0:
            self.cabeca = novo_no
            self.cauda = novo_no
        else:
            novo_no.proximo = self.cabeca
            self.cabeca.anterior = novo_no
            self.cabeca = novo_no
            
        self._tamanho += 1
    
    def inserir_fundo(self, elemento):
        novo_no = NoDuplo(elemento)

        if self._tamanho == 0:
            self.cabeca = novo_no
            self.cauda = novo_no
        else:
            novo_no.anterior = self.cauda
            self.cauda.proximo = novo_no
            self.cauda = novo_no
        
        self._tamanho += 1

    def remover_frente(self):
        if self._tamanho == 0:
            raise ValueError("O deck está vazio")
        
        elemento_removido = self.cabeca.dado
        
        if self._tamanho == 1:
            self.cabeca = None
            self.cauda = None
        else:
            self.cabeca = self.cabeca.proximo
            if self.cabeca:
                self.cabeca.anterior = None

        self._tamanho -= 1

        return elemento_removido
    
    def remover_fundo(self):
        if self._tamanho == 0:
            raise ValueError("O deck está vazio")
        
        elemento_removido = self.cauda.dado
        
        if self._tamanho == 1:
            self.cabeca = None
            self.cauda = None
        else:
            self.cauda = self.cauda.anterior
            if self.cauda:
                self.cauda.proximo = None

        self._tamanho -= 1

        return elemento_removido
    
def remover_duplicatas(fila: Deck):
    if len(fila) <= 1:
         return fila
    
    elementos_vistos = set() 
    tamanho_original = len(fila)

    for _ in range(tamanho_original):
        elemento = fila.remover_frente()
        if elemento not in elementos_vistos:
            elementos_vistos.add(elemento)
            fila.inserir_fundo(elemento)

    return fila