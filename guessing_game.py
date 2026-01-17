# Random Number Guessing Game In Python
import random
jackpot = random.randint(1, 50)
name = input("Enter your name: ")
guess = int(input("Welcome " + name + " to the game! Guess a number between 1 and 50: "))
attempts = 1
if guess>50 or guess<1:
    print("Invalid input. Please enter a number between 1 and 50.")
    guess = int(input("Enter your guess: "))
while guess != jackpot:
    if guess < jackpot:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Enter your guess: "))
    attempts += 1
print("Congratulations " + name + "! You guessed the correct number!")
print("You took " + str(attempts) + " number of attempts to guess the number.")