# W progranie chodzi o to aby obliczyć pole figury wewnętrznej opisanej w drugiej linii inputu
# oraz pole figury "zewnętrznej" której brzegi opisane są w 3 linii inputu.  kazde 2 cyfry linii inputu to współrzędne
# jednego wierzchołka. Później należy te powierzchnie przeliczyć na ilość tuszu

import math, sys

def prepareXYList(pointsList):
    listX = [pointsList[x] for x in range(0,len(pointsList),2)]
    listY = [pointsList[x] for x in range(1,len(pointsList),2)]

    return listX,listY


def computeNGonField(listX,listY):
    gaussSum = 0
    for i in range(1,len(listX)):
        minisum = listX[i] * listY[i - 1] - listX[i - 1] * listY[i]
        gaussSum += minisum


    result = math.fabs(gaussSum)/2

    return result


import sys

data = sys.stdin
testCount = int(data.readline())
text = data.read()

newList = []

for line in text.split('\n'):
    newLine = list(map(int,line.split()))
    if newLine:
        newList.append(newLine)


for test in range(testCount):
    allSurfaces  = []

    for x in range(2):
        pointsXY = newList.pop(0)
        listX,listY = prepareXYList(pointsXY)
        surfaceArea = computeNGonField(listX,listY)
        allSurfaces.append(surfaceArea)
    x = data.readline()
    black = min(allSurfaces)
    grey  = max(allSurfaces) - black

    overall = black*10 + grey*6
    print(int(overall))


##############
# Początek wstępu aby kod nie był wrażliwy na brak linii




print(newList)





