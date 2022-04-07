###########################################
# Desc: Oct 31 Demo
# Author: Hannah Noftall W0424894
###########################################
'''
Ask users to enter names of attendees
Store names in a list
Sort the list
Output the results sorted
'''
def main():
    inputValue = ""
    names = []

    while (not inputValue.lower() == "done"):
        # Ask for the name
        inputValue = input("Give me the name, or type 'Done' to exit. ")
        # Stores names in a list
        if (not inputValue.lower() == "done"):
            names.append(inputValue)
    
    # Sort function
    names.sort()

    # Ouput names
    for name in names:
        print(name)

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()