class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


def livro_ordenado(bib, new_book):
    bib.append(new_book)
    i = len(bib) -1

    while i > 0 and bib[i-1].titulo > new_book.titulo:
        bib[i] = bib[i-1]
        i -=1

    bib[i] = new_book

    return bib

l1 = Livro("Algoritmos Teoria e Prática", "Cormen")
l2 = Livro("Dom Casmurro", "Machado de Assis")
l3 = Livro("O Senhor dos Anéis", "Tolkien")

biblioteca = [l1, l2, l3]

print(f"Biblioteca Inicial: {biblioteca}")

# 2. Caso de Teste 1: Inserção no MEIO ("Harry Potter" deve entrar entre 'Dom Casmurro' e 'O Senhor...')
novo_livro_meio = Livro("Harry Potter", "J.K. Rowling")
biblioteca = livro_ordenado(biblioteca, novo_livro_meio)



print("\n--- Resultado Final ---")
# O print deve mostrar a lista perfeitamente ordenada
for livro in biblioteca:
    print(livro.titulo)