p = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
def binSe(kumpulan,target):
    low = 0
    high = len(kumpulan)-1
    a = []
    while low <= high:
        if kumpulan [low] == target:
            a.append(low)
            low += 1
        else:
            low += 1
    return a
