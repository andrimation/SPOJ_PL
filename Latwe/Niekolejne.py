# Program przyjmuje jakąś liczbę n - program ma za zadanie wypisać wszystkie
# liczby od 0 do n w taki sposób aby nie były po kolei - i żadna liczba sąsiadująca ze sobą
# nie może różnić sie od siebie o 1 - muszą różnić się o więcej np
# 4
# - 1 4 2 0 3
# Jeśli nie możliwe jest wypisanie liczb w taki sposób program powinien wyświetlić NIE.


n = int(input())

if n in [1, 2]:
    print("NIE")

else:
    result = ""
    if n % 2 != 0:
        for x in range(n-1, -1 , -2):
            print(x,end=" ")
    else:
        for x in range(n,-1,-2):
            print(x,end=" ")

    if n % 2 != 0:
        for x in range(n, -1, -2):
            print(x,end=" ")
    else:
        for x in range(n - 1, -1, -2):
            print(x,end=" ")




