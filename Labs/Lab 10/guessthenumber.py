###########################################
# Desc: Lab 10: Guess the Number
# Author: Hannah Noftall W0424894
###########################################
#imports
import random

def main():
    # Starting input
    guessesTaken = 0
    nameInput = input("Hello and welcome! What is your name? ")

    number = random.randint(1,20)
    print("Well hello there, " + nameInput + ", I am thinking of a number between 1 and 20.")

    while guessesTaken < 6:
        guess = int(input("Take a guess. "))
        guessesTaken = guessesTaken + 1

        if guess > 20:
            print("You gave me an invalid number {}. Please try again.".format(guess))
        if guess < number:
            print("Your guess is too low")
        if guess > number:
            print("Your guess is too high")
        if guess == number:
            break

    if guess == number:
        guessesTaken = str(guessesTaken)
        print("Good job, " + nameInput + "! You guessed my number in " + guessesTaken + " guesses!")

    if guess != number:
        number = str(number)
        print("Nope. The number I was thinking of was " + number)    
        playAgain()

def playAgain():
    answer = input("Would you like to play again? (y/n): ").lower()
    if answer == "y":
        main()
    elif answer == "n":
        exit()
    else: 
        print("Invalid input")
        playAgain()                            

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()