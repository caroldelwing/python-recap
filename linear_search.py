#Linear Search Algorithm
numbers = [20, 500, 10, 5, 100, 1, 50]

n = input("Type a int number: ")

found = False
for i in range(len(numbers) - 1):
    if numbers[i] == int(n):
        found = True
        break
if found == True:
    print("You won!")
else:
    print("You lost!")
