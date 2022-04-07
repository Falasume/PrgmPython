###########################################
# Desc: Results of four calculations
# Author:Hannah Noftall
########################################### 
#global variables
num1 = float(input("What is the first number?: "))
num2 = float(input("What is the second number?: "))

#main function
def main():

    # Output
    print()
    addition()
    subtraction()
    multiplication()
    division()

#calculates the process of addition
def addition():
    calculateAdd = num1 + num2
    print("{0:.2f} + {1:.2f} = {2:.2f}" .format(num1, num2, calculateAdd))
    
#calculates the process of subtraction
def subtraction():
    calculateSub = num1 - num2 
    print("{0:.2f} - {1:.2f} = {2:.2f}" .format(num1, num2, calculateSub))

#calculates the process of multiplication
def multiplication():
    calculateMulti = num1 * num2
    print("{0:.2f} * {1:.2f} = {2:.2f}" .format(num1, num2, calculateMulti))

#calculates the process of division
def division():        
    calculateDiv = num1 / num2
    print("{0:.2f} / {1:.2f} = {2:.2f}" .format(num1, num2, calculateDiv))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()