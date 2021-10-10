import sys

data = sys.stdin

text = data.read()

newText = ""

spaceChecker = False
for letter in text:
    if letter != " ":
        if spaceChecker == True:
            newText += letter.capitalize()
            spaceChecker = False
        else:
            newText += letter
    else:
        spaceChecker = True
print(newText)