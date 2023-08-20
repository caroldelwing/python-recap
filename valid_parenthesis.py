def valid_parenthesis(s):
    # If the string is odd, return false bc the pairs dont match
    if len(s) % 2 != 0:
        return False
    #Create a dict with the possible pairs of parenthesis
    dict = {"(":")", "{":"}", "[":"]"}
    #Create an empty stack to store open parenthesis
    stack = []

    #Loop through the string, add the open parenthesis to the stack
    for ch in s:
        if ch in dict.keys(): #opening parenthesis? append to stack
            stack.append(ch)
        else:
            #if we have a close parenthesis and the stack is empty, it means that we dont have an open parenthesis for that close parenthesis, return false
            if stack == []:
                return False
            #pop stack, and assign popped element to open_brac
            #check if ch is equal to the value of the dict related to the open parenthesis popped element
            #In other words, check if there's a close parenthesis that match the popped open parenthesis
            #If there's not, return false
            open_brac = stack.pop()
            if ch != dict[open_brac]:
                return False
    #if stack is empty, return True
    return stack == []

print(valid_parenthesis("((()))"))