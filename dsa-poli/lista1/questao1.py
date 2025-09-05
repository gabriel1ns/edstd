class Livro:
    def __init__(self, titulo, autor, ano, codigo):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.codigo = codigo

class Node:
    def __init__(self, livro_conc):
        self.dado = livro_conc
        self.next = None

class Metodos:
    def __init__(self):
        self.start = None

    def adicionar(self, livro_conc):
        new_node = Node(livro_conc)
        if self.start is None:
            self.start = new_node
            return
        
        current = self.start

        while current.next is not None:
            current = current.next
        current.next = new_node

    def buscar(self, titulo_p):
        current = self.start
        while current is not None:
            if current.dado.titulo == titulo_p:
                return current.dado
            current = current.next
        return None
    
    def remocao(self, codigo):
        if self.start is None:
            return

        if self.start.dado.codigo == codigo:
            self.start = self.start.next
            return
        
        last = None
        current = self.start
        
        while current is not None and current.dado.codigo != codigo:
            last = current
            current = current.next
        
        
        if current is not None:
            last.next = current.next

    def imprimir(self):
        if self.start is None:
            print("A lista está vazia.")
            return
        
        lista_str = []
        current = self.start
        while current is not None:
            lista_str.append(str(current.dado))
            current = current.next
        print(" -> ".join(lista_str))


