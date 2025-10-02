
def jacobsthal(n):

    if n < 0:
        return None
    
    # casos base

    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return 2 * jacobsthal(n-1) - jacobsthal(n-2)

print("Os 10 primeiros termos da sequência são:")
for i in range(10):
    print(f"Jacobsthal({i}) = {jacobsthal(i)}")