#Find the index of two numbers in the array, if the sum of them is equal to target
def two_sum(target, nums):

    n = len(nums)
    for i in range(n-1):
        for j in range (i+1, n):
            if nums[i] + nums[j] == target:
                return  [i, j]
    return []

target = 9
nums = [2,7,11,15]

print(two_sum(target, nums))