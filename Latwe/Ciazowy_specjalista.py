import math
testCount = int(input())

for test in range(testCount):
    x,y,z = map(int,input().split())
    partResult = ((x+y)-(z*y))/(z-1)
    result = round(12 * partResult)
    print(int(math.fabs(result)))
