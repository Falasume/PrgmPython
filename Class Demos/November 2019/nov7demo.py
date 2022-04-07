###########################################
# Desc: 
# Author: Hannah Noftall W0424894
###########################################

def main():
    # Input
    my2DList = []
    my2DList.append([10, 20, 30, 40, 50])
    my2DList.append([100, 200, 300, 400, 500])
    my2DList.append([1000, 2000, 3000, 4000, 5000])
    # Process
    
    # Output
    for row in my2DList:
        for number in row:
            print(number, end = "\t")
        print()    

    for rowIndex in range(0, len(my2DList)):
        for colIndex in range (0, len(my2DList[rowIndex])):
            #print(f"Row {rowIndex} Col {colIndex}")
            print(my2DList[rowIndex][colIndex], end = "\t")  
        print()      

    #print(my2DList[1][3])

    #print(my2DList[0])
    #print(my2DList[1])
    #print(my2DList[2])

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()