###########################################
# Desc: Calculator in Fahrenheit to Celsius
# Author:Hannah Noftall
###########################################
'''
F to C -> (F - 32) * 5/9
C to F -> (C * 9/5) + 32
'''
def main():
    # Input
    fahrenheit = float(input("What is the temperature in Fahrenheit: "))

    # Process
    result = (fahrenheit - 32) * 5/9

    # Output
    print("Result is {0:.2f} degrees in Celsius.".format(result))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()