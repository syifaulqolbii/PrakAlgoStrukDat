from math import sqrt as akar


def selesaikanABC(a, b, c):
    a = float(a)  # mengubah int menjadi float
    b = float(b)  # mengubah int menjadi float
    c = float(c)  # mengubah int menjadi float
    d = b**2 - 4*a*c
    x1 = (-b + akar(d))/(2*a)
    x2 = (-b - akar(d))/(2*a)
    hasil = (x1, x2)  # tuple yg terdiri dari 2 elemen
    return hasil


k = selesaikanABC(1, 2, 3)
print(k)
