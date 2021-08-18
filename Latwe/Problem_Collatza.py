# PRogram wykonuje ciag Collatza - i go numeruje
# n które chcemy obliczyć to jest nr iteracji w której x = 1


# Można to obliczyć funkcja rekurencyjną, albo bez zabawy pętlą while.

# Pobranie danych
testCount = int(input())

listOfNumbers = []

for test in range(testCount):
    listOfNumbers.append(int(input()))


# Obliczenia

for number in listOfNumbers:
    x = number
    n = 0
    while x != 1:
        if x % 2 != 0:
            x = 3*x+1
        else:
            x = x/2
        n +=1
    print(n)




