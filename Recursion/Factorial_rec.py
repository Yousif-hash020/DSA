def Factorial(n):
    if n==0 or n==1: # base case
        return 1
    return n * Factorial(n-1)

print(Factorial(4))