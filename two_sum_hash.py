#Find the index of two numbers in the array, if the sum of them is equal to target
#Use hash table (dict) to store the array values using index as value and number as key
def two_sum(target, nums):
    numMap = {}
    n = len(nums)
    for i in range(n):
        complement  = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i

    return []

target = 9
nums = [2,7,11,15]

print(two_sum(target, nums))