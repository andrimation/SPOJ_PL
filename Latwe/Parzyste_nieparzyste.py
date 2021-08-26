testCounter = int(input())

for test in range(testCounter):
    testList = input().split()
    for number in range(2,len(testList),2):
        print(testList[number],end= " ")

    for number in range(1,len(testList),2):
        print(testList[number], end=" ")
    print()
