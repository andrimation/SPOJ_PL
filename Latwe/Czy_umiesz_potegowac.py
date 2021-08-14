counter = int(input())
listaLiczb = []

for x in range(counter):
    potega, wykladnik = input().split()
    listaLiczb.append([int(potega),int(wykladnik)])


listaReszt = [1,2,3,0]

for liczby in listaLiczb:
    potega,wykladnik = liczby[0],liczby[1]

    # Sprawdzanie potęg
    if potega % 10 in[0,1,5,6]:
        print(potega%10)

    # Podstawa 4
    elif potega % 10 == 4:
        if wykladnik % 2 == 0:
            print(6)
        else:
            print(4)

    # Podstawa 9
    elif potega % 10 == 9:
        if wykladnik % 2 == 0:
            print(1)
        else:
            print(9)

    # Podstawy z listą reszt


    # Podstawa 2
    elif potega % 10 == 2:
        koncowki = [2,4,8,6]
        reszta = wykladnik % 4
        print(koncowki[listaReszt.index(reszta)])

    elif potega % 10 == 3:
        koncowki = [3,9,7,1]
        reszta = wykladnik % 4
        print(koncowki[listaReszt.index(reszta)])

    elif potega % 10 == 7:
        koncowki = [7,9,3,1]
        reszta = wykladnik % 4
        print(koncowki[listaReszt.index(reszta)])

    elif potega % 10 == 8:
        koncowki = [8,4,2,6]
        reszta = wykladnik % 4
        print(koncowki[listaReszt.index(reszta)])