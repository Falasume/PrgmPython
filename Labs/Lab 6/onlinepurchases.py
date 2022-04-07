###########################################
# Desc: Oct 3 Demo
# Author:Hannah Noftall
###########################################
#imports
import sys

def main():
    # Defining variable

    tax = 0
    # Input
    country = input("What country are you from?: ")
    inputTotal = float(input("What is the total of your order?: "))
    country = country.lower()

    # Process
    if country != "canada":
        print("Your total is ${0:.2f}".format(inputTotal))
        sys.exit(0)
    if country == "canada": 
        province = input("Which province are you located in?: ")
        province = province.lower()
    if province == "alberta":
        tax = 1.05
    if province == "ontario" or province == "new brunswick" or province == "nova scotia":
        tax = 1.15
    else:
        tax = 1.11
    calculateTotal = inputTotal * tax

    # Output
    print()
    print("Your total is ${0:.2f}".format(calculateTotal))
    print("Have a nice day!")
    
#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()