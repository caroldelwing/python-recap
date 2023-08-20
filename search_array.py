#Search key in an unsorted array arr
def findElement(arr, n, key):
    for i in range(n):
        if (arr[i] == key):
            return i
    #If the key is not found
    return -1

arr = [12, 34, 10, 6, 40]
key = 40
n = len(arr)

    #Search operation
index = findElement(arr, n, key)
if index != -1:
    print("Element Found at position: " + str(index + 1))
else:
        print("Element not found")