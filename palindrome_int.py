#Convert int to str, then reverse the string using str slicing
def palindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    return       False
print(palindrome(-121))

''' Using while loop+math
number = 67890
reversed_number = 0

while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
    
print(reversed_number)'''