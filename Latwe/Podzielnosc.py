testCounter = int(input())

for test in range(testCounter):
    n, x, y = map(int,(input().split()))

    answers = []

    for number in range(n):
        if number % x == 0 and number % y != 0:
            answers.append(number)

    answers.sort()

    for answer in answers:
        print(answer, end=" ")
    print()



