testCounter = int(input())

listsOfNumbers = []
for test in range(testCounter):
    listsOfNumbers.append(list(map(int, input().split())))

for subList in listsOfNumbers:
    subList = subList[1:]
    for number in subList[::-1]:
        print(number, end=" ")
    if subList != listsOfNumbers[-1]:
        print()
    else:
        pass