###########################################
# Desc: Tech Check 3
# Author: Hannah Noftall W0424894
###########################################

def main():
    # Starting Message
    print("Grade Point Calculator")
    print("----------------------")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.")

    # Defining variables
    modifierPlus = 0.3
    modifierMinus = -0.3

    # Input
    letterGrade = input("Please enter a letter grade: ").upper()
    modifierInput = input("Please enter a modifier (+, - or nothing): ").upper()

    # Process
    if letterGrade == "A":
        numberGrade = 4 
    elif letterGrade == "B":
        numberGrade = 3
    elif letterGrade == "C":
        numberGrade = 2
    elif letterGrade == "D":
        numberGrade = 1
    else:
        numberGrade = 0     

    if modifierInput == "+":
        modifierGrade = numberGrade + modifierPlus
    elif modifierInput == "-":
        modifierGrade = numberGrade + modifierMinus
    else:
        modifierGrade = numberGrade        

    # Output
    print("The number value is: {}".format(modifierGrade))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()