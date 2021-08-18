# Zadanie - przesunięcie podanych liczb w odpowiednim porządku

# Input -
# 1 linia - ilość testów
# kolejne linie - zestawy testowe złożone z liczb - każda 1 liczba zestawu określa ilość liczb w danym zestawie.

testCounter = int(input())

for test in range(testCounter):
    numbersList = list(input().split())[1:]
    numberToMove = numbersList.pop(0)
    numbersList.insert(len(numbersList),numberToMove)
    for number in numbersList:
        print(number,end=" ")
    print()