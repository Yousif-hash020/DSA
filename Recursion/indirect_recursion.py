def functionA(n):
    if n<= 0:
        return 
    
    print("A", n)
    
    return functionB(n-1)

def functionB(n):
    if n <= 0:
        return 
    
    print("B", n)
    return functionA(n-1)

functionA(5)