import sys
from numba import jit

# testCount = int(sys.stdin.readline())
# testCount = 1
# Tworzę tablcę o wymiarach ilość liter w u na ilość liter w v

@jit()
def LCS(A,B,i=0,j=0):
    if i == wordOneCount or j == wordTwoCount:
        return 0
    elif A[i] == B[j]:
        return 1 + LCS(A,B,i+1,j+1)
    else:
        return max(LCS(A,B,i+1,j),LCS(A,B,i,j+1))


testCount = int(sys.stdin.readline())


for test in range(testCount):
    wordOneCount = int(sys.stdin.readline())
    wordOne = sys.stdin.readline()
    wordTwoCount = int(sys.stdin.readline())
    wordTwo = sys.stdin.readline()

    print(LCS(wordOne,wordTwo))

