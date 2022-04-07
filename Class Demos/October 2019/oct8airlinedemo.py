###########################################
# Desc: Airline Weight Calculator
# Author:Hannah Noftall
###########################################

def main():
    surcharge = 25
    heavyLuggageLimit = 50
    maxWeight = 100

    # Input
    weightInput = float(input("What is the total luggage weight?: "))
    message = "Have a nice flight. No extra charge."

    # Process
    if weightInput > maxWeight:
        message = "Your luggage is too heavy to fly."
    elif weightInput > heavyLuggageLimit:
        message = "Have a nice flight. You have a surcharge of ${:.2f}.".format(surcharge)

    # Output
    print(message)
#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()