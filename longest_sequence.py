def long_sequence(nums):
    sum_seq = 1 #starts in one bc of the first number of array
    max_seq = 0
    n = len(nums)
    nums.sort() #sort sorts the array in place, dont assign it to a new array

    if n == 0: #check if len(nums) is 0
        return 0

    for i in range (n-1):
        if nums[i] == nums[i+1]: #ignore duplicates
            continue
        if nums[i] == nums[i+1] - 1:   #check if the numbers are sequential, if wes, add to max_seq count
            sum_seq += 1
        else: #if numbers are not sequential, update max_seq, and reset sum_seq to 1
            max_seq = max(sum_seq, max_seq) #update the max_seq variable
            sum_seq = 1

    return max(sum_seq, max_seq)

print(long_sequence([9,1,4,7,3,-1,0,5,8,-1,6]))