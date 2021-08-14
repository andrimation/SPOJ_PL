counter = int(input())
listOfNumbers = []

for x in range(counter):
    a,b = input().split()
    listOfNumbers.append([int(a),int(b)])


for nawias in listOfNumbers:
    a,b = nawias[0],nawias[1]
    done = False

    multiply = 1
    while done != True:
        x = int(a)*multiply
        if x % int(b) == 0:
            print(x)
            done = True
        else:
            multiply +=1