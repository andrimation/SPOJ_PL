import sys

data = sys.stdin
testCounter = int(data.readline())


tekst = data.read()
setOfLetters = set()
for litera in tekst:
    if not litera.isspace():
        setOfLetters.add(litera)
listOfLetters = list(setOfLetters)
listOfLetters.sort(key=lambda x: (
x.isupper(), x))  # <- tu się dzieje coś takiego że True > False - więc mniejsze - czyli zwracające false są
# na początku, a większe, czyli zwracające true są na końcu - tu na pytanie czy x.isupper() małe zwracają false -> więc idą na początek,
# sortowane alfabetycznie,
for letter in listOfLetters:
    print(letter + " " + str(tekst.count(letter)))