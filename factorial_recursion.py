def recu_factorial(n):
    if n == 1:
        return n
    else:
        return n * recu_factorial(n-1)

print(recu_factorial(5))