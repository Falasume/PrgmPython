#################################################
# Desc: Assignment 3, Prog 2: Message Redaction #
# Author: Hannah Noftall W0424894               #
#################################################

def main(): 
    while True:     
        # Input from user
        messageInput = input("Type a phrase (or type quit to exit program): ").lower()
        if messageInput == "quit":
            exit()
        
        # Output
        encryptionMethod = encryptMessageInput(messageInput)

def encryptMessageInput(messageInput):
    # Converts the input to a list containing each individual character of the string
    redactedChars = list(map(str, input("Type a comma-seperated list of letters to redact (format: x,y,z): ").split(","))) 
    redactCounter = 0

    # Removes all letters to be redacted to underscores
    for message in range(len(redactedChars)):
        while messageInput.replace(redactedChars[message], "_", 1) != messageInput:
            redactCounter += 1
            messageInput = messageInput.replace(redactedChars[message], "_", 1)

    print("Number of letters redacted: {0}".format(redactCounter))
    print("Redacted phrase: {0}".format(messageInput))
    print()        

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()