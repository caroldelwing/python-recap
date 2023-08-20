dayConversion = {
    "Mon": "Monday",
    "Tue": "Tuesday",
    "Wed": "Wednesday",
    "Thu": "Thursday",
    "Fri": "Friday",
    6: "Saturday"
}

print(dayConversion["Mon"])
print(dayConversion.get("Mon"))
print(dayConversion.get(6))
print(dayConversion.get("Lux", "Not a Valid Key"))