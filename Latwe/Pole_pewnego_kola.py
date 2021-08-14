pi = 3.141592654

R,d = input().split()
R,d = float(R),float(d)/2


# Obliczenie r2

r_sqr = (R**2) - (d**2)


smallCircleField = pi*(r_sqr)
print(round(smallCircleField,2))