def insert_end(key, arr):
    arr.append(key)

key = int(input("Enter the int number you want to insert: "))
user_input = input("Enter the list of numbers separated by comma: ").split(",")
arr = [int(x) for x in user_input]

print(key)
print(arr)

insert_end(key, arr)

print(arr)