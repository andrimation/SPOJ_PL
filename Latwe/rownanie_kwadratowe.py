import sys

# Przyjęcie danych
listOfData = []
while True:
    try:
        a,b,c = (sys.stdin.readline()).split()
        listOfData.append([float(a),float(b),float(c)])
    except:
        break

#Obliczenia
for bracket in listOfData:
    a,b,c = bracket[0],bracket[1],bracket[2]

    delta = (b**2) - (4*a*c)
    if delta < 0:
        print(0)
    elif delta == 0:
        print(1)
    else:
        print(2)
