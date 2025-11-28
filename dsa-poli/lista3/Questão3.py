import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])
    
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivo = arr[len(arr) // 2]
    esquerda = [x for x in arr if x < pivo]
    meio = [x for x in arr if x == pivo]
    direita = [x for x in arr if x > pivo]
    
    return quick_sort(esquerda) + meio + quick_sort(direita)

def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    
    min_value = min(arr)
    max_value = max(arr)
    bucket_count = len(arr)
    bucket_range = (max_value - min_value) / bucket_count + 1
    
    buckets = [[] for _ in range(bucket_count)]
    
    for num in arr:
        index = int((num - min_value) / bucket_range)
        if index >= bucket_count:
            index = bucket_count - 1
        buckets[index].append(num)
    
    for i in range(bucket_count):
        buckets[i].sort()
    
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr


algoritmos = {
    'Bubble Sort': bubble_sort,
    'Selection Sort': selection_sort,
    'Insertion Sort': insertion_sort,
    'Merge Sort': merge_sort,
    'Quick Sort': quick_sort,
    'Bucket Sort': bucket_sort
}


print("=" * 80)
print("LISTAS ALEATÓRIAS")
print("=" * 80)

tamanhos = [1000, 10000, 20000, 30000, 40000, 50000]
resultados_aleatorios = {nome: [] for nome in algoritmos.keys()}

print(f"\n{'Tamanho':<10}", end='')
for nome in algoritmos.keys():
    print(f"{nome:<15}", end='')
print("\n" + "-" * 100)

for tamanho in tamanhos:
    lista = [random.randint(1, 10000) for _ in range(tamanho)]
    
    print(f"{tamanho:<10}", end='')
    
    for nome, func in algoritmos.items():
        inicio = time.time()
        func(lista.copy())
        tempo = time.time() - inicio
        resultados_aleatorios[nome].append(tempo)
        print(f"{tempo:.4f}s{' ':<7}", end='')
    
    print()


print("\n" + "=" * 80)
print("LISTA DESCENDENTE (50.000 elementos)")
print("=" * 80)

lista_descendente = list(range(50000, 0, -1))
resultados_descendente = {}

print(f"\n{'Algoritmo':<20} {'Tempo':<15}")
print("-" * 35)

for nome, func in algoritmos.items():
    inicio = time.time()
    func(lista_descendente.copy())
    tempo = time.time() - inicio
    resultados_descendente[nome] = tempo
    print(f"{nome:<20} {tempo:.4f}s")



fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))


for nome, tempos in resultados_aleatorios.items():
    ax1.plot(tamanhos, tempos, 'o-', label=nome, linewidth=2, markersize=6)

ax1.set_xlabel('Tamanho da Lista', fontsize=11)
ax1.set_ylabel('Tempo (segundos)', fontsize=11)
ax1.set_title('Listas Aleatórias', fontsize=12, fontweight='bold')
ax1.legend()
ax1.grid(True, alpha=0.3)

nomes = list(resultados_descendente.keys())
tempos = list(resultados_descendente.values())

ax2.bar(range(len(nomes)), tempos)
ax2.set_xticks(range(len(nomes)))
ax2.set_xticklabels(nomes, rotation=45, ha='right')
ax2.set_ylabel('Tempo (segundos)', fontsize=11)
ax2.set_title('Lista Descendente (50.000 elementos)', fontsize=12, fontweight='bold')
ax2.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('comparacao_ordenacao.png', dpi=300, bbox_inches='tight')
print("\n✓ Gráfico salvo como 'comparacao_ordenacao.png'")
plt.show()


if resultados_aleatorios['Bubble Sort'][-1] > 0 and resultados_aleatorios['Quick Sort'][-1] > 0:
    speedup = resultados_aleatorios['Bubble Sort'][-1] / resultados_aleatorios['Quick Sort'][-1]
    print(f"\nPara 50.000 elementos: Quick Sort foi {speedup:.0f} mais rápido que Bubble Sort")



for nome in ['Bubble Sort', 'Insertion Sort']:
    if resultados_aleatorios[nome][-1] > 0:
        aleatorio = resultados_aleatorios[nome][-1]
        descendente = resultados_descendente[nome]
        diferenca = ((descendente - aleatorio) / aleatorio) * 100
        print(f"  {nome}: {diferenca:+.1f}% na lista descendente")

print("\n" + "=" * 80)