import sys

data = sys.stdin

first = data.readline().split()

rollNumber = int(first[1])
listToRoll = list(map(int, data.readline().split()))

for iteration in range(0, rollNumber):
    move = listToRoll.pop(-1)
    listToRoll.insert(0, move)

for number in listToRoll:
    print(number, end=" ")