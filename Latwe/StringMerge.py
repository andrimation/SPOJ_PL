


def string_merge(stringA,stringB):
    if len(stringA)> len(stringB):
        maxString = stringA
        minString = stringB
    else:
        maxString = stringB
        minString = stringA

    iterationCounter = len(minString)
    returnString = ""

    for iteration in range(0,iterationCounter):
        returnString += stringA[iteration]+stringB[iteration]

    return returnString






# Pobranie danych
testCounter = int(input())

stringList = []

for string in range(testCounter):
    stringA,stringB = input().split()
    stringList.append([stringA,stringB])

for bracket in stringList:
    print(string_merge(bracket[0],bracket[1]))


