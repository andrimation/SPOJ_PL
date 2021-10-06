# mamy w pierwszej linii - ilość zestawóœ danych

# W pierwszej linii każgego zestawu - Liczba uczestników konkursu
# w drugiej - poszczególne wyniki uzyskane przez uczestników

# na wyjściu dla każdego zestawu -> wyprintować - najwyższy wynik jako pierwszy ( jeśli jest kilka najwyższych to najpierw najwyższe,
# później kolejne wyniki odwrotnie - od najmniejszego do największego, wszystko w jednej linii np: 5 5 2 3 4 ( chyba oddzielone spacją )

import sys

data = sys.stdin
testCount = int(data.readline())
# print(testCount)

for test in range(testCount):
    for line in range(2):
        winners = []
        sortedResult = []
        data.readline()
        listOfResults = list(map(int,data.readline().split()))
        # print(listOfResults)
        try:
            maxResult = max(listOfResults)
        except:
            pass
        for x in listOfResults.copy():
            if x == maxResult:
                q = listOfResults.pop(listOfResults.index(x))
                winners.append(q)
        if listOfResults:
            listOfResults.sort()
            for x in listOfResults:
                # if x not in sortedResult:
                sortedResult.append(x)
        finalList = winners + sortedResult
        for x in finalList:
            print(x,end=" ")
        print()