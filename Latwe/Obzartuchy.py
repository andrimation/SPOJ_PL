# Wrócić do zadania z hexami !

# Wejście:
# 1 linia - liczba zestawów testowych
# 2 linia - 2 liczby oddzielone spacją - liczba gości, liczba ciastek w jednym pudełku
# N kolejnych wierszy
#   -- czasy jedzenia ciastek przez kolejnych gości ( liczba gosci definiuje ile razy należy tu pobrać informację o czasie jedzenia )


# Obliczyć ile pudełek ciastek kupić na zlot. - czyli wynik zaokrąglić w górę tak, aby był podzielny przez podaną liczbę ciastek w pudełku.

testCounter = int(input())

listOfInformations = []

# To poniżej za skomplikowane - olać słowniki itp - tak na prawdę potrzebuję tylko listy czasów gości i przez nią później będę iterował
# wszystkie pozostałe dane mam już w zmiennych.
for testNum in range(testCounter):
    guests, packSize = input().split()
    for guest in range(int(guests)):


