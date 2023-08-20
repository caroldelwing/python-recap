#There's a secret word stored in a variable
#User needs to guess the secret word
secret_word = "giraffe"

#Empty variable to store user guesses
guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

#User will be asked until answer correctly: loop!
#User only has 3 guesses
i = 0
guessed_ok = False
while guess != secret_word and i < 3:
        guess = input("Enter guess: ")
        if guess == secret_word:
            guessed_ok = True
            break
        i += 1
#
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True

if guessed_ok == False:
    print("You loose")
else:
    print("You won!")