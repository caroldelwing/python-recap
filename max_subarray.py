def max_subarray(nums):
    sum = 0
    max_sum = min(nums)
    for num in nums:
        sum = sum + num
        if sum > max_sum:
            max_sum = sum
        if sum < 0:
                sum = 0
    return max_sum

print(max_subarray([-1,-2,3,2]))