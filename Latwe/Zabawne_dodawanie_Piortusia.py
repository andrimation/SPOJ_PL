counterOfNumbers = int(input())
listOfNumbers = []

for counter in range(counterOfNumbers):
    listOfNumbers.append(int(input()))

# Sprawdzenie czy liczba jest palindromem

for number in listOfNumbers:
    if str(number) == str(number)[::-1]:
        print(number,0)
    else:
        palindrom = False
        counterOfAdds = 0
        while not palindrom:
            numberToAdd = str(number)[::-1]
            if numberToAdd[0] == 0:
                numberToAdd = numberToAdd[1:]
            add = number + int(numberToAdd)
            counterOfAdds += 1
            if str(add) == str(add)[::-1]:
                print(add, counterOfAdds)
                palindrom = True
            else:
                number = add
