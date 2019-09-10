"""
This program will assign a random number to a variable, then the user has to
input that random number by guessing. The program will tell the user if the
input is higher than the random number or lower than the random number.
This program is written by Justin Le.
"""

import random

# A random number is set to variable number, and variable guess is set to 1024
# so that the while loop after this block always run on startup.
guess = 1024
number = random.randint(0, 1023)

# While the user hasn't guessed the random number, the program will repeatedly
# ask the user to guess a number, and then the program will promptly respond
# whether the input was too high or too low based on the random number.
while guess != number:
    guess = int(input("Enter a number, preferably from 0 to 1023: "))
    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")

# After the user inputs the random number, the program will say the user was
# correct, thanks the user for playing, and ends afterwards.
print("Correct. Thank you for playing.")
