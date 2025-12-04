class Carta:
    def __init__(self, nome, vida, mana, ataque):
        self.nome = nome
        self.vida = vida
        self.mana = mana
        self.ataque = ataque

# Criando a lista de objetos
colecao = [
    Carta("Mago", 5, 1, 2), 
    Carta("Rei", 5, 1, 2), 
    Carta("Boi", 3, 3, 2), 
    Carta("Gavião", 4, 2, 1), 
    Carta("Soldado", 5, 1, 3)
]

def combinacoes_possiveis(colecao):
    comb = []
    n = len(colecao)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                
                c1 = colecao[i]
                c2 = colecao[j]
                c3 = colecao[k]

                comb.append((c1.nome, c2.nome, c3.nome))
    
    return comb

resultado = combinacoes_possiveis(colecao)

for trio in resultado:
    print(trio)
