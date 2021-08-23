import sys

data = list((sys.stdin.readline()).split())

for x in data[::-1]:
    print(x,end=" ")