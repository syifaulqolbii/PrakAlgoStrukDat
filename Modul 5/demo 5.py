class MhsTIF(object):
    def __init__(self, nama, umur, tinggal, nim):
        self.nama = nama
        self.umur = umur
        self.kotaTinggal = tinggal
        self.nim = nim


def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp


list = [MhsTIF('Ika', 10, 'Sukoharjo', 'L200200141'),
        MhsTIF('Budi', 51, 'Sragen', 'L200200169'),
        MhsTIF('Ahmad', 2, 'Surakarta', 'L200200151'),
        MhsTIF('Chandra', 18, 'Surakarta', 'L200200176'),
        MhsTIF('Eka', 4, 'Boyolali', 'L200200170'),
        MhsTIF('Fandi', 31, 'Salatiga', 'L200200189'),
        MhsTIF('Deni', 13, 'Klaten', 'L200200145'),
        MhsTIF('Galuh', 5, 'Wonogiri', 'L200200190'),
        MhsTIF('Janto', 23, 'Klaten', 'L200200195'),
        MhsTIF('Hasan', 64, 'Karanganyar', 'L200200172'),
        MhsTIF('Khalid', 29, 'Purwodadi', 'L200200189')]


def cekNim(object):
    for i in object:
        print(i.nim)


def urutNim(object):
    n = len(object)
    for i in range(n-1):
        for j in range(n-i-1):
            if object[j].nim > object[j+1].nim:
                swap(object,j,j+1)
