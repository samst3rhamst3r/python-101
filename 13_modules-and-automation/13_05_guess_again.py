# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random

min = 1
max = 10
number = random.randint(min, max)

user_input = -1
while user_input != number:
    user_input = input("Please guess a number between 1 and 10! ")
    if not user_input.isdigit():
        print("Invalid. Please input an integer.")
    else:
        user_input = int(user_input)
        if user_input < min or user_input > max:
            print(f"Input must be between {min} and {max}, inclusive.")
        elif user_input != number:
            print("Wrong! Guess again!")
        else:
            print(f"Correct! The number is {user_input}! Thanks for playing!")