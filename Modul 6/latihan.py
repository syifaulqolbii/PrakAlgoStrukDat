# Nomor 1
import time
from random import shuffle as kocok
from time import time as detak


class MhsTIF(object):
    def __init__(self, nama, nim, tinggal, us):
        self.nama = nama
        self.nim = nim
        self.tinggal = tinggal
        self.us = us


c0 = MhsTIF('Ika', 'L20019001', 'Sukoharjo', 240000)
c1 = MhsTIF('Budi', 'L20019003', 'Sragen', 230000)
c2 = MhsTIF('Ahmad', 'L20019002', 'Surakarta', 250000)
c3 = MhsTIF('Chandra', 'L20019004', 'Surakarta', 235000)
c4 = MhsTIF('Eka', 'L20019006', 'Boyolali', 240000)
c5 = MhsTIF('Fandi', 'L20019005', 'Salatiga', 250000)
c6 = MhsTIF('Deni', 'L20019007', 'Klaten', 245000)
c7 = MhsTIF('Galuh', 'L20019009', 'Wonogiri', 245000)
c8 = MhsTIF('Janto', 'L20019008', 'Klaten', 245000)
c9 = MhsTIF('Hasan', 'L20019011', 'Karanganyar', 270000)
c10 = MhsTIF('Khalid', 'L20019010', 'Purwodadi', 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9]


class Node():
    def __init__(self, data, tautan=None):
        self.data = data
        self.tautan = tautan


def cetak(head):
    curr = head
    while curr is not None:
        try:
            print(curr.data)
            curr = curr.tautan
        except:
            pass


a = Node(80)
b = Node(7)
c = Node(24)
d = Node(16)
e = Node(43)
f = Node(91)
g = Node(35)
h = Node(2)
i = Node(19)
j = Node(72)

a.tautan = b
b.tautan = c
c.tautan = d
d.tautan = e
e.tautan = f
f.tautan = g
g.tautan = h
h.tautan = i
i.tautan = j


def mergeSortLinkedList(A):
    linked = A
    try:
        daftar = []
        curr = A
        while curr:
            daftar.append(curr.data)
            curr = curr.tautan
        A = daftar
    except:
        A = A

    if len(A) > 1:
        mid = len(A) // 2
        separuhkiri = A[:mid]
        separuhkanan = A[mid:]

        mergeSortLinkedList(separuhkiri)
        mergeSortLinkedList(separuhkanan)

        i = 0
        j = 0
        k = 0
        while i < len(separuhkiri) and j < len(separuhkanan):
            if separuhkiri[i] < separuhkanan[j]:
                A[k] = separuhkiri[i]
                i = i + 1
            else:
                A[k] = separuhkanan[j]
                j = j + 1
            k = k+1

        while i < len(separuhkiri):
            A[k] = separuhkiri[i]
            i = i + 1
            k = k+1

        while j < len(separuhkanan):
            A[k] = separuhkanan[j]
            j = j + 1
            k = k+1

    for x in A:
        try:
            linked.data = x
            linked = linked.tautan
        except:
            pass


mergeSortLinkedList(a)
cetak(a)
