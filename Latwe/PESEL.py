
testCount = int(input())

numbersToMultiply = [1,3,7,9,1,3,7,9,1,3,1]

for test in range(testCount):
    pesel = str(input())
    sum = 0
    for number in range(0,11):
        sum += (int(pesel[number]) * numbersToMultiply[number])
        if sum % 10 == 0:
            print("D")
        else:
            print("N")