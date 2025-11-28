def hasPair(list, sum):
    if len(list) < 2:
        return None
    
    sorted_list = sorted(list)

    left  = 0
    right = len(sorted_list) -1

    while left < right:
        current_sum = sorted_list[left] + sorted_list[right]

        if current_sum == sum:
            return True, (sorted_list[left] + sorted_list[right])
        elif current_sum < sum:
            left +=1
        else:
            right -=1
        
    return False

'''
O método hasPair() vai combinar a ordenação e a varredura da lista com os ponteiros left e right
Dessa forma é possivel escapar da complexidade O(n^2), que é a da solução clássica desse tipo de problema usando nested loops
Esse algoritmo possui complexidade O(nlog(n)), já que criamos a lista ordenada (log(n))
e varemos ela toda em busca da soma destino: sum.
'''