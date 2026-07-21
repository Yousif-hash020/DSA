def Power(n):
    if n == 1:
        return True
    if n<= 0 or n % 2 != 0:
        return False
    return Power(n // 2)

print(Power(16))