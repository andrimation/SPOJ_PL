countOfTests = int(input())
listOfNumbers = []
for x in range(0,countOfTests):
    listOfNumbers.append(int(input()))
tuple(listOfNumbers)
for y in listOfNumbers:
    liczbaPierwsza = True
    if y == 1:
        liczbaPierwsza = False
    else:
        for z in range(2,int(y**0.5)+1):
            if y % z == 0:
                liczbaPierwsza = False
                continue
    if liczbaPierwsza:
        print("TAK")
    else:
        print("NIE")
