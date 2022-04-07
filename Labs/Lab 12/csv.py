###########################################
# Desc: File IO
# Author: Hannah Noftall W0424894
###########################################

def main():
    # Create file, mode then open file
    guestList = "guests.csv"
    mode = "a"
    fileIO = open(guestList, mode)

    # Input from user
    guestInput = input("Enter attendee's name and age (ex: Paul, 45) type quit to exit: ")
    if guestInput.lower() == "quit":
        quit()

    # Updates file and closes it when program is finished
    fileIO.write(f"{guestInput}\n")
    fileIO.close()
  
#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    while True:
        main()