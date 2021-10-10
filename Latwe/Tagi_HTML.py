import sys

data = sys.stdin

htmlCode = data.read()

newHtmlCode = ""

capitalize = False

for letter in htmlCode:
    if letter == "<":
        capitalize = True
    elif letter == ">":
        capitalize = False

    if capitalize == True:
        newHtmlCode += letter.capitalize()
    else:
        newHtmlCode += letter

print(newHtmlCode)