import math, sys

mainData = []

testCounter = int(sys.stdin.readline())

# Przyjęcie danych
for x in range(testCounter):
    listOfData = []
    numberOfPoints = sys.stdin.readline()
    for q in range(int(numberOfPoints)):
        alpha, x, y = (sys.stdin.readline()).split()
        listOfData.append([alpha, int(x), int(y)])
    if testCounter != 1:
        enterPlaceholder = sys.stdin.readline()
    mainData.append(listOfData)

result = []

# Sortowanie
for smallList in mainData:
    sortedList = []
    listofDataCopy = smallList.copy()
    while listofDataCopy:
        maxDistance = listofDataCopy[0]
        for bracket in listofDataCopy:
            if (maxDistance[1]**2 + maxDistance[2]**2)**0.5 > math.sqrt(
                    (math.fabs(bracket[1])) ** 2 + (math.fabs(bracket[2])) ** 2):
                maxDistance = bracket
        sortedList.append(maxDistance)
        listofDataCopy.remove(maxDistance)

    result.append(sortedList)

# Wyświetlenie danych
for dataSet in result:
    for bracket in dataSet:
        print(bracket[0], bracket[1], bracket[2])
    if bracket != dataSet[-1][-1]:
        print()





