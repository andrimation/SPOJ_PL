import sys

while True:
    try:
        operator,a,b = (sys.stdin.readline()).split()
        a,b = int(a),int(b)
        if operator == "+":
            print(a+b)
        elif operator == "-":
            print(a-b)
        elif operator == "/":
            print(a/b)
        elif operator == "%":
            print(a%b)
        elif operator == "*":
            print(a*b)
    except:
        break