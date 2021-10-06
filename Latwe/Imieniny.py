import sys

data = sys.stdin
testCount = int(sys.stdin.readline())

for test in range(testCount):
    osoby,cukierki = list(map(int,data.readline().split()))
    osoby = osoby-1
    if osoby == 1:
        print("TAK")
    elif cukierki % osoby == 0:
        print("NIE")
    else:
        print("TAK")

