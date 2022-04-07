###########################################
# Desc: Lab 5 Shipping Charges
# Author: Hannah Noftall W0424894
###########################################

def main():
    #Defining variables
    shipping = 10

    #Input
    inputTotal = float(input("Enter the amount for your total purchase: $"))

    #Process
    if inputTotal < 50:
        amountTotal = inputTotal + shipping
        print("An extra $10 is added for shipping costs")
        print("Your total is ${0:.2f}".format(amountTotal))
    elif inputTotal:
        print("Your total is ${0:.2f}".format(inputTotal))

    #Output
    print("Have a nice day!")
#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()