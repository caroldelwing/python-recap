#Append new employee to the file
employee_file = open("employees.txt", "a")

#Be careful, is permanent
employee_file.write("\nToby 102")

#Will overwrite all lines inside the file
#employee_file = open("employees.txt", "w")
#employee_file.write("\nToby 102")

employee_file.close()

#Create new file
employee_file = open("index.txt", "w")
employee_file.write("<p>This is HTML</p>")