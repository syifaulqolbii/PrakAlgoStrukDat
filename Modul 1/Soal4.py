from operator import le


def rerata(c):
    jumlah = 0
    for i in c:
        jumlah += i
    return jumlah/len(c)


print(rerata([1, 2, 4, 5, 6]))
