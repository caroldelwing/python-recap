def majority_element(arr):
    n = len(arr)//2 #target value, round to floor
    dict = {} #dict to store frequency of each number in arr

    for i in range(len(arr)):  #loop through array, save frequency of each number in dict
        if arr[i] in dict:
            dict[arr[i]] += 1
        else:
            dict[arr[i]] = 1

    for key,value in dict.items(): #loop through dict, check which value has the frequency. items() returns tuple of key,value
        if value > n:
            return key
    return 0

print(majority_element([1,2,3,4,4,4,4]))

'''easier way:  if an element occurs more than n/2 times in the array 
(where n is the size of the array), it will always occupy the middle 
position when the array is sorted. Then sort the array and get the mid
element:
arr.sort()
n = arr(nums)//2
return arr[n] -> is the middle element
'''