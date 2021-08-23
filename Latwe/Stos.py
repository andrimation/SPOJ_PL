import sys

inputData = list((sys.stdin.read()).split())

stack = []

for x in range(len(inputData)):
    if inputData[x] == "+":
        if inputData[x+1] not in stack:
            # print(inputData[x+1])
            stack.insert(0,inputData[x+1])
            print(":)")
        else:
            print(":(")
    elif inputData[x] == "-":
        try:
            print(stack[0])
            del stack[0]
        except:
            print(":(")
    # print(stack)