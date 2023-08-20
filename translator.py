#Rules: all vowels must become g

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou": #Convert all letters to lower, than check vowels
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation  = translation + letter
    return translation
print(translate("Gostoso"))