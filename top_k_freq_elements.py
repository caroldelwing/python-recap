def top_k_elements(nums, k):

    dict = {} #dict to store frequency of each number in nums

    for i in range(len(nums)):  #loop through array, save frequency of each number in dict
        if nums[i] in dict: #check if there's a nums key in dict, add it, and add the frequence as value
            dict[nums[i]] += 1
        else:
            dict[nums[i]] = 1
    #sort the dict according to freq of values in desc. order, items() return a list of tuples with key,value
    sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)

    answer = []
    #loop through list of tuples, append the key (number in nums) to the answer list
    for item in sorted_dict:
        if k <= 0:
            break
        k -= 1
        answer.append(item[0])
    return answer

print(top_k_elements([1,1,1,2,2,3,3,3,3], 2))