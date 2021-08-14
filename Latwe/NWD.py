# Funkcja obliczająca największy wspólny dzielnik

# wejście 1 linia - liczba testów
# kolejne linie - po 2 liczby z których należy obliczyć największy wspólny dzielnik

def nwdCounter(a,b):
    # Sprawdzenie która liczba jest większa
    nwd = 0
    if a > b:
        maxNum = a
        minNum = b
    elif a < b:
        maxNum = b
        minNum = a
    else:
        nwd = a
        return nwd

    eukidles = False
    while not eukidles:
        # print("liczymy dla ",maxNum,minNum)
        if maxNum % minNum != 0:
            rest = maxNum % minNum
            maxNum = minNum
            minNum = rest
        else:
            eukidles = True
            return minNum


testCounter = int(input())
listOfNumbers = []

for count in range(testCounter):
    a,b = input().split()
    listOfNumbers.append([int(a),int(b)])

for numbers in listOfNumbers:
    print(nwdCounter(numbers[0],numbers[1]))