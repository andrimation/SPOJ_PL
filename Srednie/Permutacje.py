import sys


# testCount = int(sys.stdin.readline())
testCount = 1
alphabet = "abcdefghij"
alphabet = list(alphabet)

for test in range(testCount):
    answers = []
    # lettersNumber = int(sys.stdin.readline())
    lettersNumber = 4
    text = alphabet[:lettersNumber]
    factorial = 1
    for x in range(1,len(text)+1):
        factorial *= x

    for letter in text.copy():
        letterToMove = text.pop(text.index(letter))
        text.insert(0,letterToMove)
        # print(text)
        for permut in range(int(lettersNumber-1)):
            for x in range(1,lettersNumber-1):
                text[x],text[x+1] = text[x+1],text[x]
                answers.append("".join(text.copy()))


answers.sort()


for element in answers:
    print(element)

# - czyli permutacje robimy tak - mamy listę [1,2,3,4] -> bierzemy 1 element z listy i permutujemy pozostałe -
# - jeśli mamy 4 obiekty na liście to główna pętla permutacji wykonuje sie silnia/(liczbaElementów)/2)
# - bo silnia z 4 jest 24 - 24/4 = 6/2 = 3
# - i dalej mamy 4 elemrnty w liście, więc wykonujemy permutację dla każdego elementu -> a dla każdego elementu
# - wykonujemy n-1! operacji permutacji, jeśli mamy 4 elementy, to np dla "a" wykonamy 3! permutacji  czyli 6
# a więc 4*6 = 24
# a że w przypadku powyżej - w ramach jednej pętli for możemy zrobić tylko text[x],text[x+1] = text[x+1],text[x] - > - bo robimy w range od 1, do liczbaZnaków -1
# to w ramach tej jednej pętli zrobimy tylko a c b d i   a c d b  - więc musimy jeszcze wykonać tę operację w ramach nad pętli w range liczba znaków - 1