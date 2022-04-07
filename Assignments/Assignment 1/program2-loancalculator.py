############################################
# Desc: Program 2 – Weekly Loan Calculator #    
# Author: Hannah Noftall                   #
############################################
'''
Print starting text

Input loan amount
Input interest rest in %
Input number of years to pay off loan

Total interest equals interest % divided by 5200
Calculate weekly payment by plugging in the numbers into the formula

Print weekly payment rounded to two decimal places
'''
def main(): 

    # Starting message of app 
    print("Weekly Loan Calculator")
    print("----------------------")

    # Input
    loanAmount = float(input("Enter the amount of loan: "))
    interestRate = float(input("Enter the interest rate (%): "))
    numOfYears = float(input("Enter the number of years to pay off loan: "))

    # Process
    totalInterest = interestRate / 5200
    weeklyPayment = (totalInterest) / (1-(1 + totalInterest)**(-52 * numOfYears)) * (loanAmount)

    # Output
    print()
    print("Your weekly payment will be: ${0:.2f}" .format(weeklyPayment))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()