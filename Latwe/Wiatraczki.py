# Wejście - przyjmujemy liczby - po 1 w linii. r > 0 - wiatraczek lewoskrętny, jeśli r < 0 - to wiatraczek prawoskrętny.

listOfData = [2,3]


# x = int(input())
#
# listOfData.append(x)



for fanNumber in listOfData:
    fanStart = [
        ["*","*"],
        ["*","*"]
        ]

    for step in range(fanNumber):
        fanStart.append([])
        fanStart.insert(0,[])
        newBracketLen = len(fanStart[step+1])

        fanStart[0] = ["?" for x in range(newBracketLen)]
        fanStart[-1] = ["?" for x in range(newBracketLen)]

        for bracket in fanStart:
            bracket.append("?")
            bracket.insert(0,"?")

        fanStart[0][0] = "*"
        fanStart[0][-1] = "*"
        fanStart[-1][0] = "*"
        fanStart[-1][-1] = "*"

        for index in range(len(fanStart)//2):
            fanStart[index][0] = "*"
            

        print()

        for element in fanStart:
            print(element)




