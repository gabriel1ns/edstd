def bucket_sort(arr):
    # verificação se a lista está vazia
    if len(arr) == 0:
        return arr
    
    # maior e menor valor do array para setar o intervalo
    min_value = min(arr)
    max_value = max(arr)
    
    #definição do numero de buckets, usando o sqrt() da lista como heuristica
    bucket_count = len(arr)
    
    #intervalo de cada bucket - somando + 1 pra nao dividir nunca por 0
    bucket_range = (max_value - min_value) / bucket_count + 1
    
    #cria-se todos os buckets necessários - ainda vazios
    buckets = [[] for _ in range(bucket_count)]
    
    for num in arr:
        #calculo de bucket, quanto menor o valor = bucket de menor indice
        index = int((num - min_value) / bucket_range)
        
        #indice nunca maior que numero de buckets
        if index >= bucket_count:
            index = bucket_count - 1
            
        #elemento vai pro bucket
        buckets[index].append(num)
    
    #ordenação individual de cada um dos buckets
    for i in range(bucket_count):
        buckets[i].sort()
    
    # junção de todos os buckets já ordenados, apenas concatenando eles.
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    #lista ordenada
    return sorted_arr
