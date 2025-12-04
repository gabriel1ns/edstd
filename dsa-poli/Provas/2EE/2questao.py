def insertion_sort(arr):
    comp = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comp += 1
            
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        
        arr[j + 1] = key

    return arr, comp

lista = [5, 2, 4, 6, 1, 3]
ordenada, comparacoes = insertion_sort(lista)
print(f"Lista: {ordenada}")
print(f"Comparações: {comparacoes}")