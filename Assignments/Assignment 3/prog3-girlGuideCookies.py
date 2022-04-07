##########################################################
# Desc: Assignment 3, Prog 3: Girl Guide Cookie Sell-off #
# Author: Hannah Noftall W0424894                        #
##########################################################

#Global variables
guides = []

def main():

    # Collects input from user
    numberOfGuides = 0
    numOfGuides = inputValidation(numberOfGuides)

    # Main function for program
    for counter in range(numOfGuides):
        name = input("Enter the name of guide #{}: ".format(counter + 1))
        try:
            boxesSold = int(input("Enter the number of boxes sold by {}: ".format(name)))
            guides.append(dict(name="{}".format(name), boxesSold=boxesSold))
            print()
        except ValueError:
            print("Error! This is not a valid entry. Please try again.")
            main()        

    # Calculates average cookie boxes sold
    total = 0
    highestSold = 0
    for counter in range(numOfGuides):
        total += guides[counter]['boxesSold']
        if guides[counter]['boxesSold'] > highestSold:
            highestSold = guides[counter]['boxesSold']
    averageSold = total / numOfGuides

    # Output statement for program
    print("The average amount of boxes sold by each guide was {:.1f}".format(averageSold))
    print()
    print("Guide \t \t  Prizes Won:")
    print("---------------------------------------------------------")

    # Calculates greatest to least guide for prizes
    for greatest in range(numOfGuides):
        if guides[greatest]['boxesSold'] == highestSold:
            print("{} \t \t - Trip to Girl Guide Jamboree in Aruba!".format(guides[greatest]['name']))
        elif guides[greatest]['boxesSold'] >= averageSold:
            print("{} \t \t - Super Seller Badge.".format(guides[greatest]['name']))
        elif guides[greatest]['boxesSold'] > 0:
            print("{} \t \t - Left over cookies.".format(guides[greatest]['name']))
        elif guides[greatest]['boxesSold'] == 0:
            print("{} \t \t - No prize.".format(guides[greatest]['name']))

# This function validates the user's input
def inputValidation(numberOfGuides):

    # Input from user for the number of guides
    try:
        numberOfGuides = int(input("Enter the number of guides selling cookies: "))
    except ValueError:
        print("Error! This is not a valid entry. Please try again.")   
        main()    
    print()
    return numberOfGuides

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()