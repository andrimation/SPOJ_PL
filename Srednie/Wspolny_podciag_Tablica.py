# W przypadku np 2 wyrazów, wspólnym podciagiem są litery które występują i w jednym i w drugim wyrazie
# - w tej samej kolejności, ale nie muszą być koło siebie  np zero i zoo -> najdłuższy wspólny podciag to zo
# W tym przypadku obliczamy LCS algorytmem z tablicą - w tablicy będziemy przechowywać wynik porównań
# występowania liter w w obu wyrazach.

import sys,numpy

data = sys.stdin.read()
print(data)


testCount = int(sys.stdin.readline())
# testCount = 1
# Tworzę tablcę o wymiarach ilość liter w u na ilość liter w v

for test in range(testCount):
    wordOneCount = int(sys.stdin.readline())
    wordOne = tuple(sys.stdin.readline())
    wordTwoCount = int(sys.stdin.readline())
    wordTwo = tuple(sys.stdin.readline())



    array = numpy.full([wordOneCount+1,wordTwoCount+1],0,dtype=int)
    # for x in range(wordOneCount+1):
    #     array.append([0 for x in range(wordTwoCount +1)])


    for x in range(1, wordOneCount + 1):
        for y in range(1, wordTwoCount + 1):
            if wordOne[x - 1] == wordTwo[y - 1]:
                array[x][y] = (array[x - 1][y - 1]) + 1

            else:
                array[x][y] = max(array[x - 1][y], array[x][y - 1])

    print(array[wordOneCount][wordTwoCount])


