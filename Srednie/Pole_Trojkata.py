import sys, math, numpy


def triangleField(pointA, pointB, pointC):
    field = math.fabs(
        ((pointB[0] - pointA[0]) * (pointC[1] - pointA[1]) - (pointB[1] - pointA[1]) * (pointC[0] - pointA[0]))) / 2
    return field


data = sys.stdin
testCount = int(data.readline())
for test in range(testCount):
    pointsListX = []
    pointsCount = int(data.readline())

    for line in range(1, pointsCount + 1):
        point = list(map(int, data.readline().split()))
        point.append(line)
        pointsListX.append(list(point))
    trianglesCount = int(pointsCount / 3)
    pointStatus = numpy.full(len(pointsListX), False, dtype=object)

    for triangle in range(trianglesCount):

        pointsListX.sort(key=lambda x: x[0])
        xMax = pointsListX[0]
        pointsListX.remove(xMax)
        xMin = pointsListX[-1]
        pointsListX.remove(xMin)

        pointsListX.sort(key=lambda x: x[1])
        yMax = pointsListX[0]

        candidates = [xMax, xMin, yMax]
        try:
            yMin = pointsListX[-1]
            candidates.append(yMin)
        except:
            pass

        if len(candidates) == 4:
            maxField = 0
            for pointC in candidates:
                if pointStatus[pointC[2] - 1] != True:
                    field = triangleField(xMax, xMin, pointC)
                    if field > maxField:
                        maxField = field
                        answer3 = pointC
        else:
            answer3 = candidates[2]

        myNumbers = [xMax[2], xMin[2], answer3[2]]
        myNumbers.sort()
        print(myNumbers[0], myNumbers[1], myNumbers[2])
        pointsListX.remove(answer3)
        pointStatus[answer3[2] - 1] = True
    print()
