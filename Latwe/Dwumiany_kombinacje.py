import math

testCounter = int(input())

listOfData =[]
for userInput in range(testCounter):
    a,b = input().split()
    a,b = int(a),int(b)
    listOfData.append([a,b])

# Obliczenia
for bracket in listOfData:
    silniaN = math.factorial(bracket[0])
    silniaK = math.factorial(bracket[1])
    silniaNK = math.factorial(bracket[0] - bracket[1])

    # for n in range(1,bracket[0]+1):
    #     silniaN *= n
    #
    # for k in range(1,bracket[1]+1):
    #     silniaK *= k

    # minus = bracket[0] - bracket[1]
    # for nk in range(1,minus+1):
    #     silniaNK *= nk

    # wynik
    print(int(silniaN/(silniaK*silniaNK)))

# Okazuje sie że użycie math.factorial() jest szybsze od policzenie silni pętlą for - fajnie