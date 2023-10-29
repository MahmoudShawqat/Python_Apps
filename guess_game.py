# guessing game :
# the game choose number between two numbers ,
# and user guess what number the computer choose

import random

n = random.randrange(1,10) # select number from 1 to 9 

print("Welcome to guessing game , you have 3 tries to guess")
tries = 2
# Take user input for the number to be guessed
guess = int(input("Enter any number: "))

# Loop until the guess is the same as the target number (n)
while tries:
    # Check if the guess is lower than the target number
    if guess < n:
        tries -= 1
        print("Too low")  # Print "Too low" if the guess is too low
        print(f"tries = {tries} left")
        guess = int(input("Enter number again: "))  # Take another input from the user
    # Check if the guess is higher than the target number
    elif guess > n:
        print("Too high!")  # Print "Too high" if the guess is too high
        print(f"tries = {tries} left")
        guess = int(input("Enter number again: "))  # Take another input from the user
        tries -= 1
    else:
        # Print "you guessed it right!!" when the correct guess is made
        print("you guessed it right!!")
        break # Break the loop if the guess is correct

print("Game Over! , answer is : ",n) # Print "Game Over! , answer is : " when the wrong guess is made

