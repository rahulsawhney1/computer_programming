#1. Write a program that prints out all even numbers between 1 and 100,000.
#2. Write a program that continually asks the user for a series of prices. 
# Keep track of the running total as the user enters prices. 
# Prompt the user after each price to see if they wish to continue entering prices. 
# When they are finished, print out the total amount entered.
#3. Write a program that asks the user for a number of days. 
# Then prompt the user for their weight on each day they specified (i.e. if they enter 7 you should ask them for 7 weight values). 
# When they are finished print out their average weight for the period in question. Sample running:

def even():
    for x in range(1, 100000):
        if x % 2 == 0:
            print(x)


def prices():
    continue_running = True
    price = 0
    while continue_running:
        price = input("Enter a price: ")
        price = price.strip()
        price = price.strip("$")
        price = price.strip(",")

        price = float(price)
        price += price
        keep_going = input("Would you like to continue?")

        if keep_going in ["no", "nah", "n"]:
            continue_running = False
            print(price)

def days():
    number_of_days = input("Please enter a number of days: ")
    number_of_days = int(number_of_days)
    total_weight = 0
    for day in range(number_of_days):
        message = "Day {}: Enter a weight: "
        message = message.format(day + 1)
        daily_weight = input(message)
        daily_weight = int(daily_weight)
        total_weight = total_weight + daily_weight
    average_weight = total_weight / number_of_days
    print(average_weight)


def days_validated():
    number_of_days = input("Please enter a number of days: ")
    number_of_days = int(number_of_days)
    total_weight = 0
    for day in range(number_of_days):
        message = "Day {}: Enter a weight: "
        message = message.format(day + 1)
        daily_weight = input(message)
        daily_weight = int(daily_weight)
        while daily_weight <=  0:
            print("Invalid, try again!")
            daily_weight = input(message)
            daily_weight = int(daily_weight)



        total_weight = total_weight + daily_weight
    average_weight = total_weight / number_of_days
    print(average_weight)


def free_fireworks():
    """
    Buy between 1 and 10 fireworks, get 0 free
Buy between 11 and 20 fireworks, get 1 free
Buy between 21 and 30 fireworks, get 3 free
Buy more than 31 fireworks, get 5 free

    Enter a quantity:  100
You are eligible for 5 free fireworks!
Would you like to calculate another quantity? (yes/no): yes
Enter a quantity:  3
Sorry, you are not eligible for any free fireworks.
Would you like to calculate another quantity? (yes/no): no'

    """
    keep_going = True
    while keep_going:
        amount_of_fireworks = input("Enter a quantity: ")
        amount_of_fireworks = int(amount_of_fireworks)

        if 1 <= amount_of_fireworks and 10 >= amount_of_fireworks:
            free_amount = 0
        elif 11 <= amount_of_fireworks and 20 >= amount_of_fireworks:
            free_amount = 1 
        elif 21 <= amount_of_fireworks and 30 >= amount_of_fireworks:
            free_amount = 3
        else:
            free_amount = 5
        message = "You are eligible for {} free fireworks!"
        message = message.format(free_amount)
        print(message)
        keep_going = input("Would you like to calculate another quantity? (yes/no): ")
        if keep_going == "no":
            keep_going = False
        else:
            keep_going = True

def buying_pokemon(pokemon, amount):
    """
    Write a function to that accepts two arguments: 
    the type of Pokemon the user wishes to purchase (as a String) and the number of Pokemon (as an integer). 
    Your function should calculate the total cost of this order and return it to the user (as a float).
    Note that if the function is called with an invalid Pokemon name (i.e. 'Bulbasaur') the function should return the value -1 to the caller. T
    The function should, however, handle uppercase and lowercase versions of the same Pokemon (i.e. both 'PIKACHU' and 'pikachu' are valid names). 
    You do not need to account for negative quantities in your function (this will be taken care of in the next problem) and you can always assume that the function will be called with an integer value representing the desired quantity.
     You only need to write the function outlined above. You will use this function to write a complete program in the next question. Be sure to comment your function using IPO notation.

    Pikachu		$10.00
    Charmander	$15.00
    Squirtle	$20.00
    """
    if pokemon.lower() ==  "pikachu":
        cost = 10
    elif pokemon.lower() == "charmander":
        cost = 15
    elif pokemon.lower() == "squirtle":
        cost = 20
    else:
        return -1
    
    cost = cost * amount
    print(cost)
    return cost

def flip_word(word):
    new_word = ""

    for letter in word:
        if letter.isupper():
            new_letter = letter.lower()
            new_word = new_word + new_letter
        else:
            new_letter = letter.upper()
            new_word = new_word + new_letter
    print(new_word)

