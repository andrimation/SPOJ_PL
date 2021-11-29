# Zadanie to rozwiążę w ten sposób - Obliczę pole Głównego trójkąta ABC
# Później obliczę pola 3 trójkątów PBC, PAC, PAB. -> jeżeli suma ich pól jest równa sumie pola ABC - punkt
# jest w polu trójkąta
# co więcej jeśli pole któregokolwiek trójkąta P` jest 0, przestaję liczyć i wiem że punkt leży na krawędzi trójkąta.
import sys, math


def triangleField(pointA, pointB, pointC):
    field = math.fabs(((pointB[0] - pointA[0]) * (pointC[1] - pointA[1]) - (pointB[1] - pointA[1]) * (pointC[0] - pointA[0]))) / 2
    return field


while True:
    pointsList = list(map(int, sys.stdin.readline().split()))
    if pointsList == [0,0,0,0,0,0,0,0]:
        break
    A = [pointsList[0], pointsList[1]]
    B = [pointsList[2], pointsList[3]]
    C = [pointsList[4], pointsList[5]]
    P = [pointsList[6], pointsList[7]]

    mainTriangleField = triangleField(A,B,C)

    smallTriangles = [[P,B,C],[P,A,C],[P,A,B]]
    smallTriangleAnswers = []
    for small in smallTriangles:
        smallField = triangleField(small[0],small[1],small[2])
        smallTriangleAnswers.append(smallField)

    if 0 in smallTriangleAnswers:
        if sum(smallTriangleAnswers) == mainTriangleField:
            print("E")
            continue
        else:
            print("O")
            continue
    elif sum(smallTriangleAnswers) == mainTriangleField:
        print("I")
        continue
    else:
        print("O")






