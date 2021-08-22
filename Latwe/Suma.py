import sys

data = sys.stdin

number = 0
results = []
while True:
    try:
        number += int(sys.stdin.readline())
        results.append(number)
    except:
        break

for result in results:
    print(result)

