def roman_to_int(s):
#s is the string representing the roman number
#dictionary storing letter/value
#Iterate through the string: if you found the value, add to result
#Some special conditions apply: IV, for example
#If the left number is smaller than right number, subtract left from right. If not, add

    roman = {"I":1,
             "V":5,
             "X":10,
             "L":50,
             "C":100,
             "D":500,
             "M":1000}
    result = 0

    for i in range(len(s)):
        if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
            result -= roman[s[i]]
        else:
            result += roman[s[i]]

    return result



print(roman_to_int("XXV"))