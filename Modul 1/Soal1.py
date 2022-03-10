def cetakSiku(x):
    p = 1
    for s in range(x):
        for q in range(p):
            print('*', end=" ")
        print(" ")
        p += 1


print(cetakSiku(6))
