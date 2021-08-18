# Gra polega na tym że każdy z graczy ma x != 0 żetonów. Ruch wykonuje gracz który ma mniej żetonów.
# - ruch polega na tym że gracz zabiera przeciwnikowi tyle żetonów ile sam posiada.
# gra kończy się gdy żaden z graczy nie może wykonać ruchu - czyli mają po tyle samo żetonów
# Wyświetlić ile pozostanie graczom żetonów po skończeniu danej partii ( testu )

# wejście 1 linia - liczba testów
# każda kolejna linia - 2 liczby w linii, każda liczba to ilość żetonów u gracza

testCounter = int(input())

results = []
for test in range(testCounter):
    graczA,graczB = input().split()
    graczA,graczB = int(graczA),int(graczB)

    while graczA != graczB:
        if graczA > graczB:
            graczA -= graczB
        elif graczA < graczB:
            graczB -= graczA
    results.append(graczA+graczB)

for result in results:
    print(result)
