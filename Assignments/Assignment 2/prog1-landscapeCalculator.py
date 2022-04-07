###########################################
# Desc: Assignment 2, Prog 1: Landscape Calculator
# Author: Hannah Noftall W0424894
###########################################
'''
Define global varibles
Collect inputs from user
Calculate the area
Calculate the grass cost by sending it to the function calculateBaseCost
Return the grass cost
Calculate the total of trees
Calculate total cost
Print the house number and total cost
'''
#Global variables
baseLabour = 1000
extraSurfaceArea = 5000 
extraAreaCost = 500
treeCost = 100
fescueRate = 0.05
bentgrassRate = 0.02
campusRate = 0.01
rate = 0

def main():
    #Input
    houseNum = int(input("Enter House Number: "))
    propDepth = float(input("Enter Property Depth (feet): "))
    propWidth = float(input("Enter Property Width (feet): "))
    typeOfGrass = input("Enter the Type of Grass (fescue, bentgrass, campus): " ).lower()
    numOfTrees = int(input("Enter the Number of Trees: "))

    #Calculate the area
    propArea = propDepth * propWidth

    #Calculate the grass cost, send it to the function calculateBaseCost
    grassCost = calculateGrassCost(propArea, rate, typeOfGrass)

    #Calculate the total of trees
    if numOfTrees > 0:
        totalTreeCost = numOfTrees * treeCost
    else:
        totalTreeCost = 0     

    #Calculate total cost
    totalCost = baseLabour + grassCost + totalTreeCost

    #Output
    print()
    print("Total cost for house {0} is: ${1:.2f}".format(houseNum, totalCost))

#Calculate grass cost
def calculateGrassCost(propArea, rate, typeOfGrass):
    #Equation for calculating grass cost
    grassCost = propArea * rate

    if typeOfGrass == "fescue":
        grassCost = propArea * fescueRate
    elif typeOfGrass == "bentgrass":
        grassCost = propArea * bentgrassRate
    else: 
        grassCost = propArea * campusRate
    
    if propArea > extraSurfaceArea:
       grassCost = grassCost + extraAreaCost 
    return grassCost

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()
    