#Basics: looping through all letters of the string
for letter in "Toronto":
    print(letter)

#Looping through itens in a list
friends = ["Jim", "Carol", "Lucas"]
for amigo in friends:
    print(amigo)

#Looping through a range, not including 10
for i in range(10):
    print(i)

#Looping through itens in a list (array), considering len of the list
for i in range(len(friends)):
    print(friends[i])

#If else inside for loop
for i in range(4):
    if i == 0:
        print("First iteration")
    else:
        print("Not first, sorry")