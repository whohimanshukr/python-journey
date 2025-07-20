"""
Project Title: Random Number Guessing Game

number_guessing.py is a simple Python program that selects a random number
between 1 and 100 using the random module.
The user tries to guess the number
by making approximations.
Results are displayed using standard print statements.

This project is built using Control Flow (if-else) and Loops in Python.

Built with 💻 by Himanshu Kumar.
"""

import random

# Header
print("Random Number Guessing Game")
print("=" * 45)
print()

# Greeting User
print("======= Welcome to Random Number Guessing Game =======")
print("I am guessing a number between 1-100")
print("Can you guess it correctly??")
print("Let's Begin\n")

# Generate Random Number
lucky_number = random.randint(1, 100)

# Attempts tried by users
attempts = 0

# Game Loop condition
while True:
    guess = int(input("Enter Your Guess (1,100): "))
    attempts = attempts + 1

    if guess < 1 or guess > 100:
        print("Please Enter a Valid Number between 1 and 100.\n")
    elif guess < lucky_number:
        print("Too Low!! Try again")
    elif guess > lucky_number:
        print("Too High!! Try again")
    else:
        print("Congratulations!!!")
        print(f"You guessed the number correctly after {attempts} attempts")
        break

print()
print("Thank You for choosing Random Number Guessing Game\n")
