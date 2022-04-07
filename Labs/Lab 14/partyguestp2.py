###########################################
# Desc: File IO
# Author: Hannah Noftall W0424894
###########################################
#imports
import sys

def main():
    # Create file, mode then open file
    guestList = "guests.csv"
    mode = "a"

    # Input from user
    try: 
        fileIO = open(guestList, mode)
        guestInput = input("Enter attendee's name and age (ex: Paul, 45) type quit to exit: ")
        if guestInput == "quit":
            quit()
    except FileNotFoundError:
        print("Unable to locate file.")
    except FileExistsError:
        print("File already exists.")
    except ValueError:
        print("Incorrect value.")
    except PermissionError:
        print("Error writing file. Check if file is closed.s")    

    # Updates file and closes it when program is finished
    fileIO.write(f"{guestInput}\n")
    fileIO.close()
  
#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    while True:
        main()