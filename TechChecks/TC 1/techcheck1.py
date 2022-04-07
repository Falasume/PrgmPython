###########################################
# Desc: Tech Check #1
# Author:Hannah Noftall
###########################################
 
def main():
    # original bill = 85
    # tax equals 15% of bill
    # tip equals 20% of bill
    # total equals the tip plus the tax + bill
    
    # Input
    bill = float(input("Please enter your orignial bill amount: "))
    
    # Process
    tax = bill * 0.15
    tip = bill * 0.20
    total = bill + tax + tip

    # Output
    print("Your orignial bill amount is: " + str(bill))
    print("Your tax is: " + str(round(tax))) 
    print("Your tip is: " + str(round(tip)))
    print("Your total is: " + str(round(total))) 

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()