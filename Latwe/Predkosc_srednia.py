testCounter = int(input())

for x in range(testCounter):
    vOne,vTwo = input().split()
    vOne,vTwo = int(vOne),int(vTwo)

    vMed = 2*((vOne*vTwo)/(vOne+vTwo))
    print(int(vMed))