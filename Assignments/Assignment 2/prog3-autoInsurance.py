###########################################
# Desc: Assignment 2, Prog 3: Auto Insurance
# Author:Hannah Noftall W0424894
###########################################
'''
Collect inputs from user
If statement for determining the gender
Send input to a function to calcuate the monthly insurance
Return the monthly insurance
Print the monthly insurance
'''
def main():
    #Input
    gender = input("Are you 'Male' or 'Female': ").lower()
    age = int(input("Enter your age: "))
    priceOfVehicle = float(input("Enter the purchase price of the vehicle: "))

    #If statement for determining the cost by gender
    if gender == "female":
        insurance = femaleCalculation(gender, age, priceOfVehicle)
    else:
        insurance = maleCalculation(gender, age, priceOfVehicle)  

    #Output
    print("Your monthy insurance will be: ${0:.2f}".format(insurance))

#Function for calulating the monthly insurance for a female
def femaleCalculation(gender, age, priceOfVehicle):    
    if age >= 15 and age < 25:
        monthlyInsurance = priceOfVehicle * 0.20 / 12 
    elif age >= 25 and age < 40:
        monthlyInsurance = priceOfVehicle * 0.15 / 12 
    else:
        monthlyInsurance = priceOfVehicle * 0.10 / 12    
    return monthlyInsurance

#Function for calulating the monthly insurance for a male
def maleCalculation(gender, age, priceOfVehicle):                      
    if age >= 15 and age < 25:
        monthlyInsurance = priceOfVehicle * 0.25 / 12 
    elif age >= 25 and age < 40:
        monthlyInsurance = priceOfVehicle * 0.17 / 12 
    else:
        monthlyInsurance = priceOfVehicle * 0.10 / 12          
    return monthlyInsurance

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()
    