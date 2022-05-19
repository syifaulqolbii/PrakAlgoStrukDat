# NO 1

##P = [2,8,15,23,37]
##Q = [4,6,15,20]
##R = gabungkanDuaListUrut(P, Q)
# print(R)

# def gabungkanDuaListUrut(A,B):
##    la = len(A); lb = len(B)
##    C = list()
##    i = 0; j = 0
##
# while i < la and j < lb:
# if A[1] < B[j]:
# C.append(A[i])
##            i += 1
# else :
# C.append(B[j])
##            j += 1
# while i < la:
# C.append(A[i])
##        i += 1
# while j < lb:
# C.append(B[j])
##        j += 1
# return C

# NO 2
# eksekusi gui shell liat di laporan
# def mergeShort(A):
# if len(A) > 1:
##        mid = len(A) // 2
##        separuhKiri = A[:mid]
##        separuhKanan = A[mid:]
##
# mergeShort(separuhKiri)
# mergeShort(separuhKanan)
##
##        i=0 ; j=0 ; k=0
# while i < len(separuhKiri) and j < len(separuhKanan):
# if separuhKiri[i] < separuhKanan[j]:
##                A[k] = separuhKiri[i]
##                i = i + 1
# else :
##                A[k] = separuhKanan[j]
##                j = j+1
# k=k+1
##
# while i < len(separuhKiri):
##            A[k] = separuhKiri[i]
##            i = i+1
##            k = k+1
##
# while j < len(separuhKanan):
##            A[k] = separuhKanan[j]
##            j = j+1
##            k = k+1
##
# NO 3
# def quickSort(A):
#     quickSortBantu(A, 0, len(A) - 1)

# def quickShortBantu(A, awal, akhir):
#     if awal < akhir:
#         titikBelah = partisi(A, awal, akhir)
#         quickSortBantu(A, awal, titikBelah -1)
#         quickSortBantu(A, titikBelah + 1, akhir)

# def partisi(A, awal, akhir):
#     nilaiPivot = A[awal]

#     penandaKiri = awal + 1
#     penandaKanan = akhir

#     selesai = False
#     while not selesai:
#         while penandaKiri <= penandaKanan and\
#               A[penandaKiri] <= nilaiPivot:
#             penandaKiri = penandaKiri + 1

#         while A[penandaKanan] >= nilaiPivot and\
#               penandaKanan >= penandaKiri:
#             penandaKanan = penandaKanan - 1
#         if penandaKanan < penandaKiri:
#             selesai = True
#         else :
#             temp = A[penandaKiri]
#             A[penandaKiri] = A[penandaKanan]
#             A[penandaKanan] = temp

#     temp = A[awal]
#     A[awal] = A[penandaKanan]
#     A[penandaKanan] = temp

#     return penandaKanan

from lat2 import MhsTIF
c0 = MhsTIF('Ika', 10, 'Sukoharjo', 240000)
c1 = MhsTIF('Budi', 51, 'Sragen', 230000)
c2 = MhsTIF('Ahmad', 2, 'Surakarta', 250000)
c3 = MhsTIF('Chandra', 18, 'Surakarta', 235000)
c4 = MhsTIF('Eka', 4, 'Boyolali', 230000)
c5 = MhsTIF('Fandi', 31, 'Salatiga', 250000)
c6 = MhsTIF('Deni', 13, 'Klaten', 245000)
c7 = MhsTIF('Galuh', 5, 'Wonogiri', 245000)
c8 = MhsTIF('Janto', 23, 'Klaten', 245000)
c9 = MhsTIF('Hasan', 64, 'Karanganyar', 270000)
c10 = MhsTIF('Khalid', 29, 'Purwodadi', 265000)
daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
