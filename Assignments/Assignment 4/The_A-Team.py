##########################################
# Desc: Assignment 4, Prog 1: The A-Team #
# Author: Hannah Noftall W0424894        #
##########################################
'''
Defining the imports
Defining variables in the main function
Validation for opening the file
Sending and recieving the original text to a function that outputs the text
Sending and recieving the altered text to a function that outputs the text 
Function for the spacer in the program
'''
# imports for program
import random

# This is the main function
def main():
    # Defining variables
    lineList = ""
    
    # Validation for opening file
    try:
        originalFile = open("ateam_Original.txt")
        lineList = originalFile.readlines()
        originalFile.close()
    except FileNotFoundError:
        print("Error opening original file.")
        exit() 
    
    # Sends and recieves the original text
    originalProcess = originalText(lineList)

    # Sends, alters and recieves the altered text
    alteredProcess = alteredText(lineList)

# This function is for the original text    
def originalText(lineList):    
    divider()
    print("Original Text")
    divider()
    for i in range(len(lineList)):
        lineList[i] = lineList[i].rstrip("\n")
        print(f"{lineList[i]}")

    for i in range(len(lineList)):
        if len(lineList[i]) -1 > 20:
            lineList[i] = lineList[i].lower()
        elif len(lineList[i]) -1 <= 20: 
            lineList[i] = lineList[i].upper()

# This function is for the altered text
def alteredText(lineList):
    random_index = random.randrange(len(lineList))
    lineList[random_index] = " "
    divider()
    print("Altered Text")
    divider()
    for i in range(len(lineList)):
        print(f"{i+1}: {lineList[i]}")

    newFile = open("ateam_New.txt",'w') 
    newFile.writelines(lineList)
    newFile.close()

# This function is a spacer for the program
def divider():
    print("---------------------------------------------")

# Program starts here    
if __name__ == "__main__":
   main()    