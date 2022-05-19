# no 1

# print("Program menghitung luas persegi")
# sisi = int(input("Masukkan sisi = "))
# luas = sisi * sisi
# print("luas persegi = sisi x sisi. Maka luas nya = ", luas, " satuan luas")

# print("Program menghitung luas lingkaran")
# r = int(input("Masukkan jari - jari(r) = "))
# pi = 3.14
# luas = pi * r * r
# print("luas lingkaran = phi x r x r. Maka luas nya = ", luas, " satuan luas")

# print("Program menghitung luas segitiga sama sisi")
# a = int(input("Masukkan alas(a) = "))
# t = int(input("Masukkan tinggi(t) = "))
# luas = 1/2 * a * t
# print("luas segitiga sama sisi = 1/2 x a x t. Maka luas nya = ", luas, " satuan luas")

# print("Program menghitung belah ketupat")
# d1 = int(input("Masukkan diagonal 1 = "))
# d2 = int(input("Masukkan diagonal 2 = "))
# luas = 1/2 * d1 * d2
# print("luas segitiga sama sisi = 1/2 x d1 x d2. Maka luas nya = ",
#       luas, " satuan luas")

# no 2

# A = [[12, 7]]
# B = [[5, 8, 1],
#      [1, 6, 7]]
# C = [[0, 0, 0]]

# for i in range(len(A)):
#     for j in range(len(B[0])):
#         for k in range(len(B)):
#             C[i][j] += A[i][k] * B[k][j]

# for c in C:
#     print(c)

# n = 7
# baris = [0 for i in range(n)]
# matriks = [baris.copy() for i in range(n)]

# for i in range(n):
#     for j in range(n):
#         if i == j:
#             matriks[i][j] = 1
# print(matriks)


# no 3
class MhsTIF(object):
    def __init__(self, nama, umur, warnaKulit):
        self.nama = nama
        self.umur = umur
        self.warna = warnaKulit


list = (MhsTIF('Ika', 10, 'Sawo matang'),
        MhsTIF('Budi', 51, 'Kuning langsat'),
        MhsTIF('Ahmad', 2, 'Gelap'),
        MhsTIF('Chandra', 18, 'Putih'),
        MhsTIF('Eka', 4, 'Putih'),
        MhsTIF('Fandi', 31, 'Kuning langsat'),
        MhsTIF('Deni', 13, 'Sawo matang'),
        MhsTIF('Galuh', 5, 'Putih'),
        MhsTIF('Janto', 23, 'Sawo matang'),
        MhsTIF('Hasan', 64, 'Kuning langsat'),
        MhsTIF('Khalid', 29, 'Gelap'))

target = 'Sawo matang'
for i in list:
    if i.warna == target:
        print(i.nama + ' kulitnya ' + target)


def swap(A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp


def urutUmur(object):
    n = len(object)
    for i in range(n-1):
        for j in range(n-i-1):
            if object[j].umur > object[j+1].umur:
                swap(object, j, j+1)


def tampilNama(object):
    for i in object:
        print(i.nama)


def tampilUmur(object):
    for i in object:
        print(i.nama + i.umur)


def tampilWarna(object):
    for i in object:
        print(i.warna)
