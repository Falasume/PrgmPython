###########################################
# Desc: Lab 8 Python List Exercises
# Author: Hannah Noftall W0424894
###########################################

def main():
    
    # Input
    list1 = [1, 2, 3]
    list2 = [1, 3, 7]
    list3 = [1, 2, 3]
    list4 = [4, 5, 6]

    # Process
    newlist1 = reverseIt(list1)
    newlist2 = firstOrLast7(list2)
    newlist3 = middleElements(list3, list4)

    # Output
    print("ReverseIt: The list forward is: " + str(list1))
    print("ReverseIt: The list reverse is: " + str(newlist1))
    print()
    print("FirstOrLast7: The intial list is: " + str(list2))
    print("FirstOrLast7: The sum of list is: " + str(newlist2))
    print()
    print("MiddleElements: The inital list is " + str(list3) + str(list4))
    print("MiddleElements: The middle elements are " + str(newlist3))

def reverseIt(list1):           
    reverseList = [list1[-1], list1[-2], list1[-3]]
    return reverseList

def firstOrLast7(list2):
    if list2[0] == 7 or list2[-1] == 7:
        return True
    else:
        return False

def middleElements(list3, list4):
    midElements1 = list3[1]
    midElements2 = list4[1]
    return [midElements1, midElements2]

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()