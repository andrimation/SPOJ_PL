import math

testCount = int(input())
answers = []
for test in range(testCount):
    listOfNumbers = list(map(int,(input().split())))
    sredniaArt = sum(listOfNumbers[1:])/listOfNumbers[0]
    closest = 0
    listOfNumbers = listOfNumbers[1:]
    for number in listOfNumbers:
        if math.fabs(sredniaArt-number) < math.fabs(sredniaArt-closest):
            closest = number
            distance = math.fabs(sredniaArt-closest)
            # I tu jest cały myk - że jak mamy 2.5 to np 3 i 2 są w tej samej odległości od 2.5 - i w tym przypadku
            # ma decydować kolejność ich wystąpienia -> czyli mamy wyświetlić pierwszą z nich w kolejności, która się pojawia.
            # Iterując po liście z góry nie wiem która liczba jest najbliżej żredniej - muszę sprawdzic wszystkie, więc tym
            # co muszę pozyskać to najmniejszy dystans - w kolejnym sprawdzeniu po prostu wyświetlić tę liczbę która po odjęciu
            # jej od średniej aryt daje ten dystans
    for number in listOfNumbers:
        if math.fabs(sredniaArt-number) == distance:
            answers.append(int(number))
            break


for element in answers:
    print(element)
