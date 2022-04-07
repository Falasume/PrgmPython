###########################################
# Desc: Lab 15 Average
# Author: Hannah Noftall W0424894
###########################################

def average(averageList):
    if len (averageList) == 0:
        raise ValueError("List is empty! Cannot average ")
    return sum(averageList) / len (averageList)

    averageList = [45,30,7,13,25,678]
    averageResult = average(averageList)

    print("The average of the list: ", round(averageResult, 2))