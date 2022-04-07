###################################################
# Desc: Assignment 4, Prog 2: Itsy Bitsy Aardvark #
# Author: Hannah Noftall W0424894                 #
###################################################

# This function is the main function
def main():
    # Defining variables
    choicesList = "" 
    story = ""

    # Validation for opening file
    try:
        choicesFile = open("the_choices_file.csv")
        choicesList = choicesFile.readlines()
        choicesFile.close()
        storyFile = open("the_story_file.txt")
        story = storyFile.read()
        storyFile.close()
    except FileNotFoundError:
        print("Error opening original file.")
        exit() 

    # Process
    for choices in range(len(choicesList)):
        choicesList[choices] = choicesList[choices].rstrip("\n")
        choicesList[choices] = choicesList[choices].split(",")

    for replace in range(7):
        story = story.replace(f"_{replace+1}_",choicesList[replace][question(choicesList[replace])].upper())
        print("")

    # Output of story to user    
    print("Your Completed Story:\n")
    print(story)

# This function is for displaying and validated the questions for the user
def questions(option):
    userInput = -1
    print(f"Please choose {option[0]}:")
    for i in range(1, 6):
        print(f"{i}) {option[i]}")
    while userInput < 1 or userInput > 5:
        userInput = int(input("Enter choice (1-5): "))
    return userInput

# Program starts here    
if __name__ == "__main__":
    main()   