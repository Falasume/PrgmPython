import math 

###################################
# Desc: Painting family room      #
# Author: Hannah Noftall          #
###################################
'''
1 Gallon of paint = 150 per square feet
2 widths, 2 lengths, 1 height
'''

def main():    
    # Input
    width1 = float(input("Input the first width of the room in feet: "))
    width2 = float(input("Input the second width of the room in feet: "))
    height = float(input("Input the room height in feet: "))

    # Process
    area1 = width1 * height * 2
    area2 = width2 * height * 2

    gallonsOfPaint = (area1 + area2) / 150

    # Output
    print("The number of gallons required is: " + str(math.ceil(gallonsOfPaint))) 

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()