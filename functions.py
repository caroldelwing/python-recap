def sayhi():
    print("Hello bae!")
#call the function to see the output
sayhi()  #Hello bae!

#put some parameters
def say_hi(name, age):
    print("Hello " + name  + " You are " + str(age))
say_hi("Carol", 33)

def cube(num):
    return num*num*num #if you dont put the return, you wont get your results
#If you add a print inside the function and after the return, it wont work bc the return breaks and end the function.
print(cube(3))



