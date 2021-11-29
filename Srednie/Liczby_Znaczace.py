import sys

testCount = int(sys.stdin.readline())

for test in range(testCount):
    testRange = list(map(int,sys.stdin.readline().split()))

    necessaryNumbersCount = 0
    for number in range(testRange[0],testRange[1]+1):
        sumOfDividers    = 0
        numberOfDividers = 0
        squareOfNumber = number**0.5

        for x in range(2,number):
            if number % x == 0:
                sumOfDividers += x
                numberOfDividers += 1
        if numberOfDividers > 0:
            if sumOfDividers/numberOfDividers <= squareOfNumber:
                necessaryNumbersCount +=1
    print(necessaryNumbersCount)


