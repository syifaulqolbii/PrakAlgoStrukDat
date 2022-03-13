from operator import le


def rerata(c):
    jumlah = 0
    for i in c:
        jumlah += i
    return jumlah/len(c)


print(rerata([1, 2, 3, 4, 5, 6, 9]))
