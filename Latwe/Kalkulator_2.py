import sys

registry = {}

while True:
    try:
        operator,a,b = (sys.stdin.readline()).split()

        if operator == "z":
            registry[str(a)] = int(b)
        elif operator == "+":
            print(int(registry[a])+registry[b])
        elif operator == "-":
            print(int(registry[a])-registry[b])
        elif operator == "/":
            print(int(registry[a])//registry[b])
        elif operator == "%":
            print(int(registry[a])%registry[b])
        elif operator == "*":
            print(int(registry[a])*registry[b])
    except:
        break