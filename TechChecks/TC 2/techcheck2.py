###########################################
# Desc: Tech Check #2
# Author:Hannah Noftall
###########################################

def main():
    ''' 
    Provincial withholding tax is 6.0% 
    Federal withholding tax is 25.0%
    Tax deduction for dependents 2.0%
    '''
    # Variables
    provDeduction = 0.06 #provincial tax deduction
    fedDeduction = 0.25 #federal tax deduction
    dependDeduction = 0.02 #dependant tax deduction

    # Starting Message
    print("Tax Withholding Calculator")
    print()

    # Input
    weeklySalary = float(input("Please enter the full amount of your weekly salary: "))
    dependentsAmount = int(input("How many dependents do you have?: "))

    # Process for deductions
    provTaxWithheld = weeklySalary * provDeduction
    fedTaxWithheld = weeklySalary * fedDeduction
    dependTaxGranted = (weeklySalary * dependDeduction) * dependentsAmount

    # Calculating totals
    totalWithheld = (provTaxWithheld + fedTaxWithheld) - dependTaxGranted
    totalTakeHome = weeklySalary - totalWithheld

    # Output
    print()
    print("Provincial Tax Withheld: ${0:.2f}" .format(provTaxWithheld))
    print("Federal Tax Withheld: ${0:.2f}" .format(fedTaxWithheld))
    print("Dependent Deduction for " + str(dependentsAmount) + " dependents: ${0:.2f}" .format(dependTaxGranted))
    print("Total Withheld: ${0:.2f}" .format(totalWithheld))
    print("Total Take-Home Pay: ${0:.2f}" .format(totalTakeHome))


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()