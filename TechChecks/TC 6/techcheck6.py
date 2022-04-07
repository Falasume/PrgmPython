###########################################
# Desc: Tech Check 6
# Author: Hannah Noftall W0424894
###########################################
import csv

def main():
    # Output intro to user
    fileIO = "TC6_monsters.csv"
    accessMode = "r"
    
    intro()
    playOrExit = input("Hit any key to continue ('Q' or 'q' to quit: ) ").lower()
    if (playOrExit == "q"):
        exit()

    initialHP = float(input("Please enter your initial hit points (1-200) "))
    spacer()
    
    
    with open(fileIO, accessMode) as monsterFile:
        csv_reader = csv.reader(monsterFile)
        row = list(csv_reader)
        print(f"{row[1]}") 
        print(f"{row[2]}")
        print(f"{row[3]}")
        print(f"{row[4]}")

    #print(f"You were attacked by a {} with a {} attack for {} damage.")

    #print(f"You were attacked by a {} with a {} attack for {} damage.")

    #print(f"You were attacked by a {} with a {} attack for {} damage.")

def intro():
    print("Welcome to the Dungeon Attack application where none shall survive! Simply try to live as long as you can.\n")

def spacer():
    print("==========================================================================================================")   

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()