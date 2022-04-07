###########################################
# Desc: Assignment 2, Prog 2: Erewhon Mobile Data Plans
# Author:Hannah Noftall W0424894
###########################################
'''
Collect input from user
Send input to a function that calculates the cost of Data Usage
Run the input data usage through an if, elif, else statement
Return data charge
Print the data charge total
'''
def main():
    #Input
    dataUsage = float(input("Enter Data Usage (Mb): "))

    totalCharge = calculateDataUsage(dataUsage)
    #Output
    print("Your Total Charge is: ${}".format(totalCharge)) 

def calculateDataUsage(dataUsage):
    #Calculate the total cost of Data Usage
    if dataUsage <= 200:
        dataCharge = 20
    elif dataUsage <= 500:
        dataCharge = dataUsage * 0.105
    elif dataUsage <= 1000:
        dataCharge = dataUsage * 0.11
    else:
        dataCharge = 118        
    return dataCharge

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()
    