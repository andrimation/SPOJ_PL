import time,random
# Czyli w zadaniu chodzi o to, że:
# -> dodajemy do siebie dwa pliki kart bibliotecznych
# czas łączenia 2 plików to jest suma ich długości.
# Jak już złączymy jakiś plik, to w kolejnym łączeniu tego pliku z innym, ten plik ma nowy czas łączenia,
# a na końcu musimy zsumować ze sobą wszystkie czasy.

# 1
# 4
# 1 2 4 7

# Problem 1 - sumując muszę wiedzieć które elementy ze sobą w danym kroku sumuję.
# i wyświetlić tę informację. Jeśli sumuję ze sobą np plik K + N, to utworzony plik
# ma numer pliku K

# Opcja pierwsza -> przyjąć pliki w wyrażeniu listownym, i połączyć je w tuple - zawierające (długość, numerPliku)
# następnie listę posortować według długości. - zamiast usuwać elementy z listy, można tworzyć nową listę za pomocą wyrażeń listownych

# I, jak zacznę sumować najmniejszy element, z innym najmniejszym, to on wciąż będzie miał swój początkowy nr ID,
# ale już w pewnym momencie, on przestanie być elementem najmniejszym, i wtedy znów należy listę sortować ( moze być tych sortowań wiele ? )

# Kolejny problem - oznaczanie elementów jako dodanych -> czy w elementach zawrzeć jakieś info o tym że zostały już dodane,
# czy zmieniać rozmiar listy ?

# Inna opcja - zawrzeć wszystkie numery na statycznej liście a na innej liście w jakiś sposób indeksami oznaczać które były użyte ?

#
# test = [(random.randint(1,40000),random.randint(0,1)) for x in range(1,100000)]
# # print(len(test))
# # # listToadd = []
# start = time.time()
# # # for x in test:
# # #     if x[1] == 1:
# # #         listToadd.append(x)
# listToadd = sorted([x for x in test if x[1] == 1])
#
# end = time.time()
# print(end-start)
# print(len(listToadd))

# Czyli wyrażenia listowne są dużo szybsze do skrócenia i uporządkowania listy. -> za pomocą wyrażeń listownych utworzyć listę
# List [wielkośćPliku, numerPliku,True/False] czy był użyty.
# - posortować listę według wielkości plików
# -, do pierwszego dodawać kolejne następne -> większe. Jak pierwszy będzie większy niż następny,
# ponownie posortować listę, ale tylko z tymi które nie były użyte. Pierwszego nie oznaczać jako użyty, bo jak przestanie
# być najmniejszy, to ma trafić do sortowania

import sys,numpy


# testCount = int(sys.stdin.readline())
testCount = 1
result = 0
for test in range(testCount):
    steps = []
    # filesCount = int(sys.stdin.readline())
    filesCount = 10
    # filesList = sorted([[y,x+1,False] for x,y in enumerate(list(map(int,sys.stdin.readline().split())))],key=lambda x:x[0])
    filesList = sorted([[y,x+1,False] for x,y in enumerate(list(map(int,"17 40 58 26 81 36 36 28 28 8".split())))],key=lambda x:x[0])
    # print(filesList)

    while True:
        # print(filesList)
        smaller = filesList[0]
        smaller[2] = True
        try:
            nextItem    = next(x for x in filesList if x[2] == False)
        except:
            break
        nextItem[2] = True

        smaller[0] = smaller[0] + nextItem[0]
        result += smaller[0]
        steps.append([sorted([smaller[1],nextItem[1]])])
        smaller[2] = False
        filesList = sorted([x for x in filesList if x[2] == False])



print(result)
for element in steps:
    print(element[0][0], element[0][1])

# I jak to zrobić szybciej ???