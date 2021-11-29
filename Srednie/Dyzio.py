import sys,math

testCount = int(sys.stdin.readline())


for test in range(testCount):
    numbersRange = list(map(int,sys.stdin.readline().split()))

    primeNums = 0
    for number in range(numbersRange[0],numbersRange[1]+1):
        prime = True
        for testNumber in range(2,number):
            if number % testNumber == 0:
                prime = False

        if prime:
            primeNums+=1
    print(primeNums)