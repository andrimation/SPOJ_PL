#SkarbFinder

# Pobranie danych -
# 1 linia - ilość testów
# kolejna linia - liczba lini w danym teście
        # linie testu....
# kolejna linie - z liczbą danych w kolejnym teście... itd

# Obliczenia - program na podstawie cząstkowych danych ma obliczyć położenie punktu
# 0 - +y
# 1 - -y
# 2 - -x
# 3 - +x
# - odcytując kolejne liczby z linii, program będzie bądź, to dodawał bądź odejmował, do x albo y

# następnie program zwraca położeniue punktu na osi xy - z tym że najpierw musimy zwróćić ilość krokóœ pólnoc-południe, a później ilość kroków wschód-zachód


# Pobranie danych
testCounter = int(input())

dataList = []

for test in range(testCounter):
    dataList.append([])
    numberOfLines = int(input())
    for line in range(numberOfLines):
        direction,steps = input().split()
        dataList[test].append([int(direction),int(steps)])


# Obliczenia
results = []

for testBracket in dataList:
    x = 0
    y = 0
    for dataBracket in testBracket:
        if dataBracket[0] == 0:
            y += dataBracket[1]
        elif dataBracket[0] == 1:
            y -= dataBracket[1]
        elif dataBracket[0] == 2:
            x -= dataBracket[1]
        elif dataBracket[0] == 3:
            x += dataBracket[1]
    results.append([y,x])


# Wyjście wyników

for bracket in results:
    # - na przyszłość - umieszczać to jeszcze w partii obliczeń
    if bracket[0] > 0:
        print(0,bracket[0])
    elif bracket[0] < 0:
        print(1, -1*bracket[0])
    if bracket[1] > 0:
        print(3,bracket[1])
    elif bracket[1] < 0:
        print(2,-1*bracket[1])
    elif bracket[0] == 0 and bracket[1] == 0:
        print("studnia")

    # no właśnie - bo w tym zadaniu za to czy wartość x/y jest dodatnia czy ujemna odpowiada "kierunek" - on jest minusem albo plusem,
    # zaś wartość liczby w tym przypadku jest zawsze bezwzględna bo to tylko ilość kroków
