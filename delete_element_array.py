def delete_element( arr, key):
    arr.remove(key)
user_input = input("Enter the list of numbers separated by comma: ").split(",")
arr = [int(x) for x in user_input]
key = int(input("Enter the int number you want to delete: "))

print(key)
print(arr)

delete_element(arr, key)

print(arr)


'''Manual way:
# Example array
arr = [1, 2, 3, 4, 5]

# Index of the element to delete
index_to_delete = 2

# Shift elements to the left of the deleted element
for i in range(index_to_delete, len(arr) - 1):
    arr[i] = arr[i + 1]

# Truncate the array by removing the last element
arr.pop()

# Print the updated array
print(arr)'''