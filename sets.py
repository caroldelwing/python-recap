month = ["January", "January", "February", "March"]
set_month = set(month)
print(set_month)

# Sets are unordered and its elements are unchangeable
# Items cannot be changed, only added/removed

for element in set_month:
    print(element)

# You can add/remove new values to a set
set_month.add("April")

# But you cannot control the order
print(set_month)
