import sys

data = sys.stdin

list = list(map(float,data.read().split()))
a,b,c = list[0],list[1],list[2]

if a == 0 and c-b != 0:
    print("BR")
elif a == 0 and c-b == 0:
    print("NWR")
else:
    x = (c-b)/a
    format(x,"2f")
    print(round(x,2))