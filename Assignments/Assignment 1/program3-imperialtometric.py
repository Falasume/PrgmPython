###################################################
# Desc: Program 3 - Imperial to Metric Conversion #     
# Author: Hannah Noftall                          #
###################################################
'''
Print starting text

Input number of tons
Input number of stones
Input number of pounds
Input number of ounces

Calculate total ounces
Convert total ounces to total kilos
Calculate resulting tons
Calculate resulting kilos
Calculate resulting grams

Print metric tons, kilos and grams 
'''
def main():
    # Starting message of app
    print("Imperial to Metric Conversion")
    print("-----------------------------")

    # Input
    impTons = float(input("Enter the number of ton(s): "))
    impStones = float(input("Enter the number of stone(s): "))
    impPounds = float(input("Enter the number of pound(s): "))
    impOunces = float(input("Enter the number of ounce(s): "))

    # Process
    # Calculate total ounces
    totalOunces = (35840 * impTons) + (224 * impStones) + (16 * impPounds) + impOunces      
    # Convert total ounces to total kilos
    totalKilos = totalOunces / 35.274     

    # Calculate resulting tons
    metricTons = int(totalKilos / 1000)                                 
    # Calculate resulting kilos
    metricKilos = int(totalKilos - (metricTons * 1000)) 
    # Calculate resulting grams               
    metricGrams = float(totalKilos - ((metricTons * 1000) + metricKilos)) * 1000           

    # Output
    print()
    print("The metric weight is {0} metric tons, {1} kilos, and {2:.1f} grams.".format(metricTons, metricKilos,metricGrams))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()