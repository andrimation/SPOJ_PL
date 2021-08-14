# Program - przyjmuje najpierw cyfrę określającą ilość zestawów danych
# Dalej przyjmuje co linijka jeden zestaw danych - wielkich liter

# Jeżeli w danym zestawie danych ( czyli linijce ) występuje więcej niż 2 razy jakaś litera, należy zwrócić Tą literę i cyfrę jej wystąpień

# Przyjęcie danych przez program
counter = int(input())
listOfTexts = []

for x in range(counter):
    listOfTexts.append(input())

# Zwrócenie skróconego textu

for text in listOfTexts:
    letters = [[text[0],1]]
    newWord = ""

    counter = 0
    for letter in text[1:]:
        if letter != letters[counter][0]:
            letters.append([letter,1])
            counter +=1
        else:
            letters[counter][1] += 1


    for nawias in letters:
        if nawias[1] > 2:
            newWord += f"{nawias[0]}{nawias[1]}"
        else:
            newWord += f"{str(nawias[0])*nawias[1]}"
    print(newWord)