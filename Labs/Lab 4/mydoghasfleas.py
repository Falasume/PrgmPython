###########################################
# Desc: My dog has fleas
# Author:Hannah Noftall
###########################################

def main():
    # Input
    userInput = input("Enter a word or short phrase: ")
    # Process
    
    # Output
    print("You typed: " + userInput)
    print("All lowercase: " + userInput.lower())
    print("All uppercase: " + userInput.upper())
    print("Lowercase \"o's\": " + str(userInput.count("o")))
    print("Is alphanumeric (True or False): " + str(userInput.isalpha()))
    print("All \"s's\" will become \"z's\": " + userInput.replace("s", 'z'))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()