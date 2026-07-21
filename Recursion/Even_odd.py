def is_Even(n):
    if n<= 0:
        return False
    
    print("even", n)
    return is_Odd(n-1)

def is_Odd(n):
    if n<= 0:
        return False
    print("Odd", n)
    return is_Even(n-1)

is_Even(12)