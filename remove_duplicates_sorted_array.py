#Remove duplicates of a number in an array
def remove_duplicates(nums):
    k = 1
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            nums[k] = nums[i+1]
            k += 1
    return k

print(remove_duplicates([2,2,2,2,3]))

'''easier solution using while loop:
i = 1
while i < len (nums):
    if nums[i] == nums [i-1]:
        nums[i].pop()
    else:
        i += 1        
return len(nums)

or using sort in place with [:]
nums[:] = set(nums)
		return len(nums)'''