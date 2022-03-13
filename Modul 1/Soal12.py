import random
rdm = random.randint(1, 100)
print("""Permainan tebak angka.\nSaya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak.""")
m = "Masukkan tebakan ke-"
o = ":> "
c = 1
d = str(c)
for i in range(1, 100):
    e = (m + d + o)
    a = int(input(e))
    c += 1
    d = str(c)
    if (a < rdm):
        print("Itu terlalu kecil. Coba lagi.")
    elif (a > rdm):
        print("Itu terlalu besar. Coba lagi.")
    elif (a == rdm):
        print("Ya. Anda benar")
        break
