#Open the file and read
employee_file = open ("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)

#Return if you can read from the file
print(employee_file.readable())

#Read the file, one line -> Be careful because the commands follow a sequence
#print(employee_file.read())

#print(employee_file.readline()) #First line
#print(employee_file.readline()) #Second Line (sequential)
#print(employee_file.readlines()) #Read lines and put them in an array
#print(employee_file.readlines()[1])  #Read index 1 line

#Close the file at some point
employee_file.close()