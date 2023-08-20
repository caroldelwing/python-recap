#Ask user for input: goal and deadline
#Return how many days till the deadline
#For date handling, use the datetime module, with the datetime class
from datetime import datetime

user_input = input("Enter your goal and a deadline separated by colon:\n")
#Create a list from the input
input_list = user_input.split(":")

#Assign each list element to a variable
goal = input_list[0]
deadline = input_list[1]

#Convert the string deadline to a real date using datetime module, datetime class, strptime function
deadline_date = datetime.strptime(deadline,"%d.%m.%Y")

#Store today's date to a variable
today_date = datetime.today()

#Calculate how many days until deadline
number_of_days = deadline_date - today_date

print(f"Time remaining for your goal: {goal} is {number_of_days.days} days.")
