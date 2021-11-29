import sys,numpy


testCount = int(sys.stdin.readline())
# testCount = 1

for test in range(testCount):
    result = 0
    steps = []
    filesCount = int(sys.stdin.readline())
    # filesCount = 10
    filesList = [[y,x+1,False] for x,y in enumerate(list(map(int,sys.stdin.readline().split())))]
    # filesList = [[y,x+1,False] for x,y in enumerate(list(map(int,"17 40 58 26 81 36 36 28 28 8".split())))]


    while True:
        smaller = min( x for x in  filesList if x[2] != True)
        smaller[2] = True
        try:
            nextItem    = min( x for x in  filesList if x[2] != True)
        except:
            break
        nextItem[2] = True
        smaller[0] = smaller[0] + nextItem[0]
        result += smaller[0]
        steps.append([sorted([smaller[1],nextItem[1]])])
        smaller[2] = False



print(result)
for element in steps:
    print(element[0][0], element[0][1])
