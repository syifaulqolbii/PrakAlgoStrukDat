# NOMER 1
#
# class MhsTIF(object):
#     def __init__(self, nama, umur, tinggal, nim):
#         self.nama = nama
#         self.umur = umur
#         self.kotaTinggal = tinggal
#         self.nim = nim


# def swap(A, p, q):
#     tmp = A[p]
#     A[p] = A[q]
#     A[q] = tmp


# list = (MhsTIF('Ika', 10, 'Sukoharjo', 'L200200141'),
#         MhsTIF('Budi', 51, 'Sragen', 'L200200169'),
#         MhsTIF('Ahmad', 2, 'Surakarta', 'L200200151'),
#         MhsTIF('Chandra', 18, 'Surakarta', 'L200200176'),
#         MhsTIF('Eka', 4, 'Boyolali', 'L200200170'),
#         MhsTIF('Fandi', 31, 'Salatiga', 'L200200189'),
#         MhsTIF('Deni', 13, 'Klaten', 'L200200145'),
#         MhsTIF('Galuh', 5, 'Wonogiri', 'L200200190'),
#         MhsTIF('Janto', 23, 'Klaten', 'L200200195'),
#         MhsTIF('Hasan', 64, 'Karanganyar', 'L200200172'),
#         MhsTIF('Khalid', 29, 'Purwodadi', 'L200200189'))


# def cekNim(object):
#     for i in object:
#         print(i.nim)


# def urutNim(object):
#     n = len(object)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if object[j].nim > object[j+1].nim:
#                 swap(object, j, j+1)

# NOMER 2

from random import shuffle as kocok
from time import time as detak


def BubbleSort(value):
    for passnum in range(len(value)-1, 0, -1):
        for i in range(passnum):
            if value[i] > value[i+1]:
                temp = value[i]
                value[i] = value[i+1]
                value[i+1] = temp


DaftarAngka = [24, 8, 30, 99, 3, 14, 11, 20]
BubbleSort(DaftarAngka)

a = DaftarAngka
DaftarAngka1 = [50, 51, 52, 53]
BubbleSort(DaftarAngka1)

b = DaftarAngka1
DaftarAngka2 = (a+b)
BubbleSort(DaftarAngka2)

c = DaftarAngka2
print(c)

# NOMER 3


def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A, j, j+1)


def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)


def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai


def swap(A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp


def cariPosisiYangTerkecil(A, p, q):
    posisiYangTerkecil = p
    for i in range(p+1, q):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
        return posisiYangTerkecil


k = []
for i in range(1, 6001):
    k.append(i)
kocok(k)

u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak()
bubbleSort(u_bub)
ak = detak()
print('bubble: %g detik' % (ak-aw))
aw = detak()
selectionSort(u_sel)
ak = detak()
print('selection: %g detik' % (ak-aw))
aw = detak()
insertionSort(u_ins)
ak = detak()
print('insertion: %g detik' % (ak-aw))
