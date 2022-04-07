###########################################
# Desc: Tech Check 4
# Author:Hannah Noftall W0424894
###########################################

#FUNCTION
def main():
    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.\n")

    letterGradePROG = input("Please enter a letter grade for PROG1700: ").upper()
    modifier = input("Please enter a modifier (+, - or nothing): ")

    letterGradeNETW = input("Please enter a letter grade for NETW1700: ").upper()
    modifier = input("Please enter a modifier (+, - or nothing): ")

    letterGradeOSYS = input("Please enter a letter grade for OSYS1200: ").upper()
    modifier = input("Please enter a modifier (+, - or nothing): ")

    letterGradeWEBD = input("Please enter a letter grade for WEBD1000: ").upper()
    modifier = input("Please enter a modifier (+, - or nothing):  ")

    letterGradeCOMM = input("Please enter a letter grade for COMM1700: ").upper()
    modifier = input("Please enter a modifier (+, - or nothing): ")

    letterGradeDBAS = input("Please enter a letter grade for DBAS1007: ").upper()
    modifier = input("Please enter a modifier (+, - or nothing): ")

    gradeCalculate = calculateGrade(letterGradePROG, letterGradeNETW, letterGradeOSYS, letterGradeWEBD, letterGradeCOMM, letterGradeDBAS)  

    #totalAverage = letterGradePROG + letterGradeNETW + letterGradeOSYS + letterGradeWEBD + letterGradeCOMM + letterGradeDBAS

    # Output final message and result, with formatting
    print("****************************************")
    print("The numeric value for PROG1700: {0}".format(gradeCalculate))
    print("The numeric value for NETW1700: {0}".format(gradeCalculate))
    print("The numeric value for OSYS1200: {0}".format(gradeCalculate))
    print("The numeric value for WEBD1000: {0}".format(gradeCalculate))
    print("The numeric value for COMM1700: {0}".format(gradeCalculate))
    print("The numeric value for DBAS1007: {0}".format(gradeCalculate))
'''
    print("==================================================")
    print("Your grade point average for the semester is: {0:.1f}".format(totalAverage))
    print("==================================================")
'''
def calculateGrade(letterGradePROG, letterGradeNETW, letterGradeOSYS, letterGradeWEBD, letterGradeCOMM, letterGradeDBAS):
    # Determine base numeric value of the grade
    if letterGradePROG == "A":
        numericGradePROG = 4.0
    elif letterGradePROG == "B":
        numericGradePROG = 3.0
    elif letterGradePROG == "C":
        numericGradePROG = 2.0
    elif letterGradePROG == "D":
        numericGradePROG = 1.0
    elif letterGradePROG == "F":
        numericGradePROG = 0.0
    else:
        print("You entered an invalid letter grade.")
    return numericGradePROG

    if letterGradeNETW == "A":
        numericGradeNETW = 4.0
    elif letterGradeNETW == "B":
        numericGradeNETW = 3.0
    elif letterGradeNETW == "C":
        numericGradeNETW = 2.0
    elif letterGradeNETW == "D":
        numericGradeNETW = 1.0
    elif letterGradeNETW == "F":
        numericGradeNETW = 0.0
    else:
        print("You entered an invalid letter grade.")
    return numericGradeNETW

    if letterGradeOSYS == "A":
        numericGradeOSYS = 4.0
    elif letterGradeOSYS == "B":
        numericGradeOSYS = 3.0
    elif letterGradeOSYS == "C":
        numericGradeOSYS = 2.0
    elif letterGradeOSYS == "D":
        numericGradeOSYS = 1.0
    elif letterGradeOSYS == "F":
        numericGradeOSYS = 0.0
    else:
        print("You entered an invalid letter grade.")
    return numericGradeOSYS

    if letterGradeWEBD == "A":
        numericGradeWEBD = 4.0
    elif letterGradeWEBD == "B":
        numericGradeWEBD = 3.0
    elif letterGradeWEBD == "C":
        numericGradeWEBD = 2.0
    elif letterGradeWEBD == "D":
        numericGradeWEBD = 1.0
    elif letterGradeWEBD == "F":
        numericGradeWEBD = 0.0
    else:
        print("You entered an invalid letter grade.")
    return numericGradeWEBD

    if letterGradeCOMM == "A":
        numericGradeCOMM = 4.0
    elif letterGradeCOMM == "B":
        numericGradeCOMM = 3.0
    elif letterGradeCOMM == "C":
        numericGradeCOMM = 2.0
    elif letterGradeCOMM == "D":
        numericGradeCOMM = 1.0
    elif letterGradeCOMM == "F":
        numericGradeCOMM = 0.0
    else:
        print("You entered an invalid letter grade.")   
    return numericGradeCOMM

    if letterGradeDBAS == "A":
        numericGradeDBAS = 4.0
    elif letterGradeDBAS == "B":
        numericGradeDBAS = 3.0
    elif letterGradeDBAS == "C":
        numericGradeDBAS = 2.0
    elif letterGradeDBAS == "D":
        numericGradeDBAS = 1.0
    elif letterGradeDBAS == "F":
        numericGradeDBAS = 0.0
    else:
        print("You entered an invalid letter grade.")                
    return numericGradeDBAS

    # Determine whether to apply a modifier
    '''
    if modifier == "+":
        if letterGrade != "A" and letterGrade != "F": # Plus is not valid on A or F
            numericGrade += 0.3
    elif modifier == "-":
        if letterGrade != "F":     # Minus is not valid on F
            numericGrade -= 0.3
    '''

#PROGRAM STARTS HERE
if __name__ == "__main__":
    main()