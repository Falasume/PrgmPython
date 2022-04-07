###########################################
# Desc: 
# Author: Hannah Noftall W0424894
###########################################

def main():
    lab9Part1(10)
    lab9Part2()
    lab9Part3()

def lab9Part1(finalNumber):
    counter = 0
    while(counter < finalNumber):
        print(counter ** 2)
        counter += 1

def lab9Part2():
    char = ""        
    word = input("What is your name: ")
    for char in word:
        print(char)

def lab9Part3():
    sum = 0
    for i in range(0, 10):
        if i % 2 == 0:
            sum = sum + i
            print(sum)


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()