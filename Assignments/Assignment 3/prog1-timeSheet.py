##########################################
# Desc: Assignment 3, Prog 1: Time Sheet #
# Author: Hannah Noftall W0424894        #
##########################################

# Global variables    
hoursWorked = []

def main():
    # Input from user with validation
    try:
        for day in range(5):
            hoursInput = int(input("Enter hours worked on Day #{}: ".format(day + 1)))
            hoursWorked.append(hoursInput)
    except ValueError:
        print("Error! This is not a valid entry. Please try again.")   
        main()    

    # Spacer for the program
    divider()

    # Output to user
    calculateHighestHours()
    calculateTotalHours()
    calculateAverageHours()
    allStackedDays()

# This function calculates the most hours worked on x day(s)
def calculateHighestHours():
    highestHours = 0
    for day in range(5):
        if hoursWorked[day] >= highestHours:
            highestHours = hoursWorked[day]
    
    print("The most hours worked was on:")
    for day in range(5):
        if hoursWorked[day] == highestHours:
            print("Day #{} - {} hours.".format(day + 1, hoursWorked[day]))

    # Spacer for the program
    divider()

# This function calculates the total number of hours worked for the week
def calculateTotalHours():
    totalHours = 0
    for day in range(5):
        totalHours += hoursWorked[day]
    print("The total number of hours worked was: {}".format(totalHours))

# This function calculates the average hours worked for the week
def calculateAverageHours():
    totalHours = 0
    for day in range(5):
        totalHours += hoursWorked[day]
    print("The average number of hours worked each day was: {:.1f}".format(totalHours / 5))

    # Spacer for the program
    divider()

# This function calculates any days that was worked less than 7 hours
def allStackedDays():    
    slackedDays = []
    print("Days you slacked off (i.e. worked less than 7 hours):")
    for day in range(5):
        if hoursWorked[day] < 7:
            slackedDays.append(day)
    if len(slackedDays) > 0:
        for day in slackedDays:
            print("Day #{} - {} hours.".format(day + 1, hoursWorked[day]))
    else:
            print("You didnt slack off this week!")
    
# This function is a seperator    
def divider():
    print("--------------------------------------------------------")
    
#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.        
if __name__ == "__main__":
    main()