###########################################
# Desc: Functions Review.
#
# Author: Not me
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # Input
    number1 = getValidNumber("1")
    number2 = getValidNumber("2")
    # Process
    addResult = myAdd(number1, number2)
    modResult = myMod(number1, number2)

    # Output
    print("The addition result is {}".format(addResult))
    print("The mod result is {}".format(modResult))

# Prompt user for a valid number.
def getValidNumber(numLabel):
    userInput = ""
    while (not userInput.isnumeric()):
        # Keep prompting for a valid number
        userInput = input("Give me number {}? ".\
            format(numLabel))
        if (userInput.isnumeric()):
            break
        else:
            print("You gave me an invalid number {}. Please try again."\
                .format(numLabel))
    
    return int(userInput)

# This is my Adding function. It's purpose is to add two numbers.
def myAdd(userInput1, userInput2):
    result = userInput1 + userInput2
    return result

# This is my mod function. It will return the remainder of dividing the two numbers.
def myMod(userInput1, userInput2):
    return userInput1 % userInput2

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()