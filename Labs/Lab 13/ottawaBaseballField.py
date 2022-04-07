########################################
# Desc: Lab 13: Ottawa Baseball Fields #
# Author: Hannah Noftall W0424894      #
########################################
# imports for program
import csv

# Main function
def main():
    # Variable declaration
    fileIO = "Ottawa_Ball_Diamonds.csv"
    accessMode = "r"

    # User input
    userInput = input("What type of fields do you want listed: Softball, Baseball, or T-Ball?: ").lower()
    
    # Output
    readFile = readCSV(fileIO, accessMode, userInput)

# Reads CSV file 
def readCSV(fileIO, accessMode, userInput):
    if userInput == "t-ball" or userInput == "tball":
        with open(fileIO, accessMode) as myFile:
            dataFromCSV = csv.reader(myFile)
            for row in dataFromCSV:
                tballRow = "T-Ball"
                if tballRow in row:
                    print(f"{row[2]}, {row[5]}")
    if userInput == "baseball":
        with open(fileIO, accessMode) as myFile:
            dataFromCSV = csv.reader(myFile)
            for row in dataFromCSV:
                baseballRow = userInput
                if baseballRow in row:
                    print(f"{row[2]}, {row[5]}")
    if userInput == "softball":
        with open(fileIO, accessMode) as myFile:
            dataFromCSV = csv.reader(myFile)
            for row in dataFromCSV:
                softballRow = userInput
                if softballRow in row:
                    print(f"{row[2]}, {row[5]}")

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()