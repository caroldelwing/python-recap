def containsDuplicate(nums):
  n = len(nums)
  for i in range(n-1): #Loop through all elements but the last
    for j in range(i+1,n): #Loop from the second to last elements and compare if its equal
      if nums[i] == nums[j]:
        return True
  return False

  ''' Second solution: faster
      return len(set(nums)) != len(nums)

    Third solution also using set
    hashset = set()
    for i in nums:
      if i in hashset:
        return True
      hashset.add(i)
    return False'''

nums=[2,14,18,22,22]
print(containsDuplicate(nums))