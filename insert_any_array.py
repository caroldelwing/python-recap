#Insert key, in position p, of an array arr

def insert_any(key, pos, arr):
    #Easy way arr.insert(pos,key)
    #Manual way
    arr.append(None)
    for i in range(len(arr)-1, pos, -1):
        arr[i] = arr[i-1]
    arr[pos] = key

#Prompt user for the values
key = int(input("Enter the int number you want to insert: "))
user_input = input("Enter the list of numbers separated by comma: ").split(",")
arr = [int(x) for x in user_input] #Convert input to a list of int
pos = int(input("Enter the position in which you want to insert the number: "))

print("Before insertion")
print(arr)

insert_any(key, pos, arr)

print("After insertion")
print(arr)