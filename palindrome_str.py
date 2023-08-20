#Return if is a palindrome, removing all non alfhanum chars
def palindrome(x):
#Create a new string
    new_x = ''
#Remove all non alnum chars
    for i in x:
        if i.isalnum():
            new_x += i
#Convert to lower, and compare reverse
    if new_x.lower() == new_x.lower()[::-1]:
        return True
    return       False
print(palindrome("race a car"))