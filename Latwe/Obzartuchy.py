# Wrócić do zadania z hexami !

# Wejście:
# 1 linia - liczba zestawów testowych
# 2 linia - 2 liczby oddzielone spacją - liczba gości, liczba ciastek w jednym pudełku
# N kolejnych wierszy
#   -- czasy jedzenia ciastek przez kolejnych gości ( liczba gosci definiuje ile razy należy tu pobrać informację o czasie jedzenia )


# Obliczyć ile pudełek ciastek kupić na zlot. - czyli wynik zaokrąglić w górę tak, aby był podzielny przez podaną liczbę ciastek w pudełku.

testCounter = int(input())

listOfInformations = []

numberOfSecondsInDay = 24*60*60

# Przyjęcie danych i stworzenie listy z informacjami - Pod-lista o inteksie testNum - zawiera wszystkie dane dla jednego testu
for testNum in range(testCounter):
    listOfInformations.append([])
    guests, packSize = input().split()
    guests, packSize = int(guests), int(packSize)
    listOfInformations[testNum].append({'guests':int(guests),"pack_size":int(packSize)})
    listOfGuestsTimes = []
    for guest in range(guests):
        listOfGuestsTimes.append(input())
    listOfInformations[testNum].append(listOfGuestsTimes)

# Wykonanie obliczeń dla każdego testu
for testNum in range(testCounter):
    informations = listOfInformations[testNum]

    cookiesEaten = 0

    for guest in informations[1]:
        guestCookies = numberOfSecondsInDay // int(guest)
        cookiesEaten += guestCookies


    if cookiesEaten % informations[0]["pack_size"] == 0:
        cookiesToBuy = cookiesEaten/informations[0]["pack_size"]
    else:
        cookiesToBuy = (cookiesEaten // informations[0]["pack_size"]) + 1
    print(int(cookiesToBuy))











