###########################################
# Desc: Sept 16 Demo
# Author:Hannah Noftall
###########################################

def main():

    # Input
    num1 = float(input("Tell me the first number? "))
    num2 = float(input("Tell me the second number? "))
    
    # Process
    result = round(num1 + num2, 2)
    print("Result type is " + str(result))
    # Output
    print("The result is " + str(result))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()