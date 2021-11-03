testCounter = int(input())

for test in range(testCounter):
    a,b = list(map(int, input().split()))
    print(a * b)