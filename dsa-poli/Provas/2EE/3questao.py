def sort(list):
    if len(list) <= 1:
        return list
    pivot = list[int(len(list)/2)]

    left = [x for x in list if x < pivot]
    middle = [x for x in list if x == pivot]
    right = [x for x in list if x > pivot]

    return sort(left) + middle + sort(right)

lista = [5, 2, 4, 6, 1, 3]
ordenada = sort(lista)
print(f"Lista: {ordenada}")
