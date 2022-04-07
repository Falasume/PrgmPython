###########################################
# Desc: 
# Author: Hannah Noftall W0424894
###########################################

def main():
    # Variable declaration
    my2DList = []
    my2DList.append(["Steven, Matt, Greg, Max, Josh"])
    my2DList.append(["Morgan, Laura, Hannah, Grant, Nick"])
    my2DList.append(["Katelyn, Cole, Connor, Devin, Colton, Xavier"])
    my2DList.append(["Kieran, Brett, Parker"])

    # Output
    for rowIndex in range(0, len(my2DList)):
        for colIndex in range(0, len(my2DList[rowIndex])):
            print(f"Pod {rowIndex + 1} students: ")
            for counter in range(1):
                print(my2DList[rowIndex][colIndex], end = "\n")
                print()
                
#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()