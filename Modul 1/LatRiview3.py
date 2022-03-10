def ucapkanSalam():
    print('Assalamualaikum')


def sapa(nama):
    ucapkanSalam()  # memanggila fungsi
    print('Halo', nama)
    print('Selamat belajar')


def kuadratkan(b):
    h = b*b
    return h


print(sapa('Syifaul'), kuadratkan(2))
