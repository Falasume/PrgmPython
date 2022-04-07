###########################################
# Desc: Tech Check 5
# Author: Hannah Noftall W0424894
###########################################

# main function
def main():
    # Input
    firstNum = getValidNumber("first")
    secondNum = getValidNumber("second")

    # Process
    calcHCD = getHighestCommonDivisor(firstNum, secondNum)

    # Output
    print("The Highest Common Divisor of {0} and {1} is: {2}".format(firstNum, secondNum, calcHCD))
    tryAgain()

# function to validate user input
def getValidNumber(number):
    userInput = ""
    while (not userInput.isnumeric()):
        # Keep prompting for a valid number
        userInput = input("Enter the {} number: ".format(number))
        if (userInput.isnumeric()):
            break
        else:
            print("ERROR! Enter a valid {} number".format(number))
    
    return int(userInput)

# function to calculate the highest common divisor
def getHighestCommonDivisor(firstNum, secondNum):
    if firstNum > secondNum:
        smallerNum = secondNum
    else:
        smallerNum = firstNum

    for smallerNum in range(1, smallerNum + 1):
        if((firstNum % smallerNum == 0) and (secondNum % smallerNum == 0)):
           highestCommonDivisor = smallerNum

    return highestCommonDivisor

# play again function
def tryAgain():
    print()
    answer = input("Would you like to try again? (y/n): ").lower()
    if answer == "y":
        main()
    elif answer == "n":
        exit()
    else: 
        print("Invalid input")
        tryAgain()                     

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()

    