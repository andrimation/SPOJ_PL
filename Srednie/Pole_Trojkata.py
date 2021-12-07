import sys, math


def triangleField(pointA, pointB, pointC):
    field = math.fabs(
        ((pointB[0] - pointA[0]) * (pointC[1] - pointA[1]) - (pointB[1] - pointA[1]) * (pointC[0] - pointA[0]))) / 2
    return field


data = sys.stdin
testCount = int(data.readline())
for test in range(testCount):
    pointsListX = []
    pointsCount = int(data.readline())

    pointsListX = [list(map(int, (data.readline().split() + [x]))) for x in range(1, pointsCount + 1)]



    pointsListX.sort(key=lambda x: x[0])

    pointsListY = pointsListX.copy()
    pointsListY.sort(key=lambda x: x[1])
    pointsListYrev = pointsListY.copy()
    pointsListYrev.reverse()

    trianglesCount = int(pointsCount / 3)
    pointStatus = [False for x in range(pointsCount)]

    xMaxIteration = 0
    xMinIteration = 0

    yMaxIteration = 0
    yMinIteration = 0

    for x in range(trianglesCount):
        xMax = pointsListX[xMaxIteration]
        if pointStatus[xMax[2] - 1] == True:
            while True:
                xMaxIteration += 1
                xMax = pointsListX[xMaxIteration]

                if pointStatus[xMax[2] - 1] == False:
                    break
        pointStatus[xMax[2] - 1] = True

        xMin = pointsListX[((-1) * xMinIteration) - 1]
        if pointStatus[xMin[2] - 1] == True:
            while True:
                xMinIteration += 1
                xMin = pointsListX[((-1) * xMinIteration) - 1]
                if pointStatus[xMin[2] - 1] == False:
                    break

        pointStatus[xMin[2] - 1] = True

        yMaxIterationSave = yMaxIteration

        yMax = pointsListY[yMaxIteration]
        if pointStatus[yMax[2] - 1] == True:
            while True:
                yMaxIteration += 1
                yMax = pointsListY[yMaxIteration]
                if pointStatus[yMax[2] - 1] == False:
                    break

        yMinIterationSave = yMinIteration

        yMin = pointsListYrev[yMinIteration]
        if pointStatus[yMin[2] - 1] == True:
            while True:
                yMinIteration += 1
                yMin = pointsListYrev[yMinIteration]
                if pointStatus[yMin[2] - 1] == False:
                    break

        candidates = [yMax, yMin]

        maxField = 0
        for pointC in candidates:
            field = triangleField(xMax, xMin, pointC)
            if field > maxField:
                maxField = field
                answer3 = pointC

        myNumbers = [xMax[2], xMin[2], answer3[2]]
        myNumbers.sort()
        print(myNumbers[0], myNumbers[1], myNumbers[2])

        pointStatus[answer3[2] - 1] = True

    print()
