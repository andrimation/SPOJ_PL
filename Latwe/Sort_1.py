import math, sys

dataInput = []
lineCounter = 0
for line in sys.stdin:
    dataInput.append((line.strip()).split())


    lineCounter +=1
print(dataInput)







mainData = []

for test in range(testCounter):
    listofData = []
    numberOfPoints = int(input())
    for point in range(numberOfPoints):
        alpha,x,y = input().split()
        listofData.append([alpha,int(x),int(y)])
    print()
    mainData.append(listofData)

# print(mainData,"main data")


result = []


for smallList in mainData:
    sortedList = []
    # print(smallList, "small list")
    listofDataCopy = smallList.copy()
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



    result.append(sortedList)
# print(result,"Result")


for dataSet in result:
    dataSet.reverse()
    for bracket in range(len(dataSet)):
        for x in range(3):
            if x != 2:
                print(dataSet[bracket][x],end=" ")
            else:
                print(dataSet[bracket][x],end="")
        if bracket != len(dataSet):
            print()
        else:
            pass
    print()

# print(result)







