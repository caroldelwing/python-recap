def bubble_sort(arr):
    n = len(arr)

    for i in range(n): #Outer loop gets each element of arr
        for j in range(0, n - i - 1):  #Don't consider last elements of arr, bc they're are ordered
            #Inner loop analyzes the element of outer loop and next element, and swap them if needed
            if arr[j] > arr[j + 1]:
                # Swap the elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)

print("Sorted array:", numbers)