#easy way for exponencials
print(2**3)

#Creating a function for doing the same
def raise_to_power(base, pow):
    result = 1
    for i in range(pow):
        result = result * base
    return result

print(raise_to_power(2, 3))