import math
testCounter = int(input())



listofData = []

for test in range(testCounter):

    numberOfPoints = int(input())
    for point in range(numberOfPoints):
        alpha,x,y = input().split()
        listofData.append([alpha,int(x),int(y)])
    print()


for test in range(testCounter):
    sortedList = []
    listofDataCopy = listofData.copy()
    while listofDataCopy:
        maxDistance = listofDataCopy[0]
        # print(maxDistance)
        for bracket in listofDataCopy:
            # print(listofDataCopy)
            # print(bracket)
            # print(maxDistance)
            # print(maxDistance[1],maxDistance[2],bracket[1],bracket[2])
            if (math.fabs(maxDistance[1]) + math.fabs(maxDistance[2])) < (math.fabs(bracket[1])+math.fabs(bracket[2])):
                maxDistance = bracket

        sortedList.append(maxDistance)
        listofDataCopy.remove(maxDistance)


for bracket in range(len(sortedList)):
    for x in range(3):
        if x != 2:
            print(sortedList[bracket][x],end=" ")
        else:
            print(sortedList[bracket][x],end="")
    if bracket != len(sortedList):
        print()
    else:
        pass









