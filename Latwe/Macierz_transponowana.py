import sys

data = sys.stdin

columns,rows = map(int,(data.readline().split()))

array = []

for info in range(columns):
    array.append(data.readline().split())

transposedArray = []

for x in range(rows):
    transposedArray.append([])
    for y in range(columns):
        transposedArray[x].append(array[y][x])

for bracket in transposedArray:
    for element in bracket:
        print(element,end=" ")
    print()
