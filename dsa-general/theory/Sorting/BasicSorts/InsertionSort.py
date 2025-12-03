def insertion_sort(list):
    comp = 0
    for i in range(1, len(list)):
        temp = list[i]
        j = i -1
        while temp < list[j] and j > -1:
            comp+=1
            list[j+1] = list[j]
            list[j] = temp
            j -=1
    return list,comp

print(insertion_sort([0,2,98,1,3,65,32]))