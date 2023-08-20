#Uses hash table
def groupAnagram(strs):

    strs_dict = {} #create an empty dir to store the key (sorted str) and values (lists of anagrams)
    for word in strs:
        sorted_word = "".join(sorted(word)) #sorted returns a list of chars, then we use join to make it a str again
        if sorted_word not in strs_dict: #if the sorted word is not in the dict, we add it as key and with value of empty list
            strs_dict[sorted_word] = []
        strs_dict[sorted_word].append(word) #then we add the word as a value of the list

    return  list(strs_dict.values()) #then, return only the values of the dicts, as lists


print(groupAnagram(["eat","tea","tan","ate","nat","bat"]))