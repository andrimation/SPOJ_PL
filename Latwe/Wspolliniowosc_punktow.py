import sys,math

mainData = sys.stdin

testCounter = int(mainData.readline())

for test in range(testCounter):
    data = mainData.readline().split("\t")
    # print(data)
    listOfPoints = []
    for iter in range(3):
        pointA = [math.fabs(int(data.pop(0))),math.fabs(int(data.pop(0)))]
        listOfPoints.append(pointA)
    results = []
    listOfPoints.sort(key= lambda x: math.fabs(x[0]) + math.fabs(x[1]))
    # print(listOfPoints)
    firstDistance = math.sqrt((listOfPoints[2][0]-listOfPoints[0][0])**2 + (listOfPoints[2][1]-listOfPoints[0][1])**2)
    # print(firstDistance)
    results.append(firstDistance)
    secondDistance = math.sqrt((listOfPoints[2][0] - listOfPoints[1][0]) ** 2 + (listOfPoints[2][1] - listOfPoints[1][1]) ** 2)
    # print(secondDistance)
    results.append(secondDistance)
    thirdDistance = math.sqrt((listOfPoints[1][0] - listOfPoints[0][0]) ** 2 + (listOfPoints[1][1] - listOfPoints[0][1]) ** 2)
    # print(thirdDistance)
    results.append(thirdDistance)
    results.sort()
    if results[0] + results[1] == results[2]:
        print("TAK")
    else:
        print("NIE")


