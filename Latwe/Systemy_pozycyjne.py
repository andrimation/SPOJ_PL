# Program zamienia liczbę dziesiętną typu float na liczbę szesnastkową i jedenastkową

def converDectToHex(decimal):
    hexInfo = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}


    returnNumber = ""
    while decimal > 0:
        divisionRest = decimal % 16
        decimal = decimal // 16
        divisionRest = divisionRest
        decimal = decimal

        # print("division rest", divisionRest)
        # print("decimal", decimal)

        if divisionRest in list(hexInfo.keys()):
            returnNumber += hexInfo[divisionRest]
        else:
            returnNumber += str(divisionRest)

    returnNumber = returnNumber[::-1]
    return returnNumber


def converDectToElevens(decimal):
    elevensInfo = {10:"A"}

    returnNumber = ""
    while decimal > 0:
        divisionRest = decimal % 11
        decimal = decimal // 11
        divisionRest = divisionRest
        decimal = decimal

        # print("division rest", divisionRest)
        # print("decimal", decimal)

        if divisionRest in list(elevensInfo.keys()):
            returnNumber += elevensInfo[divisionRest]
        else:
            returnNumber += str(divisionRest)

    returnNumber = returnNumber[::-1]
    return returnNumber


testCounter = int(input())

listOfNumbers = []

for test in range(testCounter):
    listOfNumbers.append(int(input()))

for number in listOfNumbers:
    print(converDectToHex(number), converDectToElevens(number))