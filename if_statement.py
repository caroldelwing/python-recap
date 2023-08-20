is_male = True
is_tall = False

if is_male or is_tall:
    print("You are male or tall")
else:
    print("You neither male or tall")

if is_male and is_tall:
    print("You are male AND tall")
else:
    print("You are either not male or tall or both")

if is_male and is_tall:
    print("You are male AND tall")
elif is_male and not(is_tall):
    print("You are male but not tall")
elif not (is_male) and is_tall:
    print("You are not male but tall")
else:
    print("You are not male and not tall")