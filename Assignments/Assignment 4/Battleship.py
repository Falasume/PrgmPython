##########################################
# Desc: Assignment 4, Prog 3: Battleship #
# Author: Hannah Noftall W0424894        #
##########################################
'''
Defining global variables
Defining variables within the main function
Validation for opening the file
Process for the game i.e. mapping the game, mapping hit or miss, and checking for win or lose
Output to user if they won or lost
'''
# Global variables
nameReference = ["A","B","C","D","E","F","G","H","I","J"] 
numReference = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9}
shotReference = ["·","·","O","X"]

# This is the main function
def main():
    # Defining variables
    missiles = 30
    shipMap = "" 
    gameWon = False

    # Validation for opening file
    try:
        originalFile = open("map.txt")
        shipMap = originalFile.readlines()
        originalFile.close()
    except FileNotFoundError:
        print("Error opening original file.")
        exit()

    # Process    
    for index in range(len(shipMap)):
        shipMap[index] = shipMap[index].rstrip("\n")
        shipMap[index] = shipMap[index].split(",")
    while missiles != 0 and gameWon == False:
        print("Let's play Battleship!")
        print("You have 30 missiles to fire to sink all five ships.")
        print(f"Missiles remaining: {missiles}\n")
        plotMap(shipMap)
        shot = input("Choose your target! (Ex: E6, A9): ").upper()
        shipMap[numReference[shot[0]]][int(shot[1])] = int(shipMap[numReference[shot[0]]][int(shot[1])]) + 2
        missiles -= 1
        gameWon = True
        for index in range(0,10):
            for gameMap in range(0,10):
                if shipMap[index][gameMap] == "1":
                    gameWon = False
    
    # Output to user
    if gameWon:
        print("YOU WIN!")
    else:
        print("YOU LOSE!")   

# This function
def plotMap(ships):
    print("   0 1 2 3 4 5 6 7 8 9")
    for i in range(0,10):
        print(f"{nameReference[i]} ", end="")
        for x in range(0,10):
            print(f" {shotReference[int(ships[i][x])]}", end="")
        print("")

# Program starts here    
if __name__ == "__main__":
    main()   