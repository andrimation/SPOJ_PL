# Program działa dla dowolnej wielkości macierzy ( nie tylko 3 wiersze jak w zadaniu, z tym że algorytm chyba mógłby być lepszy )

import sys, itertools

data = sys.stdin

testCounter = int(data.readline())
rows, columns = data.readline().split()
rows, columns = int(rows), int(columns)   # Coś jest nie tak z wejsciem - problem z drugim testem 

for test in range(testCounter):
    array = []
    for lines in range(rows):
        array.append(data.readline().split())

    band = []

    band.append(array[0])
    for number in range(1, rows - 1):
        band.append(array[number][-1])
    arrayReversed = array[-1]
    arrayReversed.reverse()
    band.append(arrayReversed)
    for number in range(2, rows):
        band.append(array[-number][0])
    bandFlatten = list(
        itertools.chain(*band))  # Pamietać że przy użyciu itertools.chain(*data) przed data MUSI BYĆ GWIAZDKA !

    # print(bandFlatten)

    firstElement = bandFlatten[0]
    del bandFlatten[0]
    bandFlatten.append(firstElement)

    bandFlatten.reverse()  # I teraz na przemian - iteruję - najpierw elementy mid - ile ich jest, później pobieram jedną pełną listę, później znów elementy mid
    # i znóœ jedną pełną listę ( a obróciłem ją zeby zacząć sobie od początku

    # print(bandFlatten)

    try:
        for iter in range(1, len(array) - 1):
            array[iter][0] = bandFlatten[iter - 1]
    except:
        pass

    if columns == 2:
        array[-1] = bandFlatten[len(array) - 2:len(array[0])]
    else:
        array[-1] = bandFlatten[len(array)-2:len(array[0])+1]

    counter = 2
    try:
        for iter in range(len(array) + int(len(array[0]) / 2), len(bandFlatten) - len(array[0])):
            # print(iter)
            # print(bandFlatten[iter])
            array[-counter][-1] = bandFlatten[iter]
            counter += 1
    except:
        pass

    array[0] = bandFlatten[len(bandFlatten)-len(array[0]):len(bandFlatten)]
    array[0].reverse()

for line in array:
    for element in line:
        print(element,end= " ")
    print()
