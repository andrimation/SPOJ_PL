# Wejście - przyjmujemy liczby - po 1 w linii. r > 0 - wiatraczek lewoskrętny, jeśli r < 0 - to wiatraczek prawoskrętny.
import math

# Przyjęcie danych
listOfData = []
number = int(input())
while number != 0:
    listOfData.append(number)
    number = int(input())

for fanNumber in listOfData:
    fanStart = [
        ["*", "*"],
        ["*", "*"]
    ]

    for step in range(int(math.fabs(fanNumber))-1):
        fanStart.append([])
        fanStart.insert(0, [])
        newBracketLen = len(fanStart[step + 1])

        fanStart[0] = ["?" for x in range(newBracketLen)]
        fanStart[-1] = ["?" for x in range(newBracketLen)]

        for bracket in fanStart:
            bracket.append("?")
            bracket.insert(0, "?")

        fanStart[0][0] = "*"
        fanStart[0][-1] = "*"
        fanStart[-1][0] = "*"
        fanStart[-1][-1] = "*"

        if fanNumber > 0:
            char1 = "*"
            char2 = "."
        else:
            char1 = "."
            char2 = "*"

        for iterOne in range((len(fanStart)//2)-1):
            # print(iterOne)
            fanStart[iterOne+1][0] = char1
            fanStart[-(iterOne+1)-1][0] = char2

            fanStart[0][-(iterOne+1)-1] = char1
            fanStart[0][iterOne+1] = char2

            fanStart[-(iterOne+1)-1][-1] = char1
            fanStart[iterOne+1][-1] = char2

            fanStart[-1][iterOne+1] = char1
            fanStart[-1][(-iterOne-1)-1] = char2


# Wyświetlenie wyniku
    for element in fanStart:
        for char in element:
            print(char,end="")
        print()
    print()