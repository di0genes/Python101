# Kacey Mullenhoff
# Number Guessing Game (Number Wizard)
# Guess the number the user has chosen


import random

def main():
    # Initialize 
    playing_game = "y"
    #Introduction
    print("Welcome to Number Wizard! Guess a number!")
    NOT_YET_GUESSED = -1
    lowest_guess = NOT_YET_GUESSED
    
    # Call game
    while playing_game == "y":
        guesses = game()
        if (lowest_guess == NOT_YET_GUESSED or guesses < lowest_guess):
            lowest_guess = guesses
    
    # Accept input for loop
        playing_game = str(input("Would you like to play again? y/n: "))
    # Otherwise, don't play again    
    print("Thanks for playing!")
    print (f"Your best score is: {lowest_guess}")
    
    
#Define the game function 
def game():
    total = 1
    # enter the guess
    guess= int(input("Please enter your guess (1-10): "))

    #generate number
    number=random.randint(1, 10)
    
    #Test for correctness
    while guess != number:
        print(f"Sorry, that is incorrect. You have guessed {total} times.")
        ### Increment number of attempts ###
        total += 1
        ### Try again ###
        guess= int(input("Please enter your new guess (1-10): "))

    #If successful, print congrats 
    print(f"Congratulations! You guessed the magic number in {total} guesses!")
    print(f"The Magic Number Is: {number},", end = " ")

    #even or odd
    if (number % 2) == 0:
        print( "which is an even number.")
    else:
        print("which is an odd number.")
    return total

main()
