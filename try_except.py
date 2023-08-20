try:
    num = (int(input("Enter a number: ")))
    print(num)
    #num2 = 10/0
except  ValueError: #You can specify the type of error you are getting
    print("Invalid Input")
except ZeroDivisionError as err:
    print(err)