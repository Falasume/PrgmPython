##################################################
# Desc: Program 1 – Hipster's Local Vinyl Record #    
# Author: Hannah Noftall                         #
##################################################
'''
Print starting text

Input Customer's name
Input kilometer distance for delivery
Input cost of records purchased

Calculate the distance
Calculate the record cost
Calculate the total

Print ending text
Print name with purchase summary
Print delivery cost
Print cost with tax
Print total cost
'''
def main():
    # Variables
    tax = 1.14 # Tax is 14% therefore 1.14
    distance = 15 # Delivery is $15 per kilometer

    # Starting text
    print("Hipster's Local Vinyl Records - Customer Order Details")
    print("------------------------------------------------------")

    # Input
    name = input("Enter the customer's name: ")
    kilometerDistance = float(input("Enter the distance for delivery in kilometers: "))
    costOfRecords = float(input("Enter the cost of records purchased: "))

    # Process
    calculateDistance = kilometerDistance * distance
    calculateRecord = costOfRecords * tax
    calculateTotal = calculateDistance + calculateRecord

    # Output
    print()
    print("Purchase summary for " + name + ":")
    print("-----------------------------------")
    print("Delivery cost: ${0:.2f}" .format(calculateDistance))
    print("Record cost: ${0:.2f}" .format(calculateRecord)) 
    print("Total cost: ${0:.2f}" .format(calculateTotal))


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()