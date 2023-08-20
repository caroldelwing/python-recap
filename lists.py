friends = ["Kevin", "Karen", "Jim", "Toby"]
numbers = [1, 2, 3,4]
print(max(numbers))

print(friends[0]) #prints out kevin
print(friends[-1])  #prints out toby
print(friends[1:3]) #3 is not included
friends[0] = "Me"
print(friends)

friends.extend(numbers)
print(friends)

friends.append("Creed")
print(friends)

friends.remove("Creed")
#friends.clear() -> removes all elements
friends.pop() #removes last element
print(friends)
print(friends.index("Me"))
print(friends.count("Karen"))

friends = ["Kevin", "Karen", "Jim", "Toby"]
friends.sort() #need to sort first and then print
print(friends)

numbers = [1, 2, 3,4]
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
print(numbers2)