# import the random module, which includes functions related to generating pseudo-random numbers
import random

# generate two pseudo-random numbers between 1 and 10 inclusive
rand1 = random.randint(1,10)
rand2 = random.randint(1,10)

# ask the user to guess the numbers.
guess1 = input("Guess a number between 1 and 10, inclusive: ")
guess2 = input("Guess another number between 1 and 10, inclusive: ")

# check whether the user guessed correctly
if guess1.isnumeric() and int(guess1) > 0 and int(guess1) < 11:
    if guess2.isnumeric() and int(guess2) > 0 and int(guess2) < 11:
        if int(guess1) == rand1 and int(guess2)  == rand2:
            print("Right!")
        if int(guess1) != rand1 or int(guess2) != rand2:
            print("Totally wrong!")
        elif int(guess1) == rand1 or int(guess2) == rand2:
            print("Partially right!")
    else:
        print("Bad second number!")
else:
    print("Bad first number!")
print("Done!")