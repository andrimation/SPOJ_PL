listaLiczb = []

ilePrzypadkow = int(input())
for x in range(ilePrzypadkow):
    listaLiczb.append(int(input()))

for liczba in listaLiczb:
    silnia = 1
    if liczba < 10 and liczba != 0:
        for x in range(1,liczba+1):
            silnia *= x
        print((silnia//10)%10,silnia%10)
    elif liczba >= 10:
        print(0,0)

    elif liczba == 0:
        print(0,1)