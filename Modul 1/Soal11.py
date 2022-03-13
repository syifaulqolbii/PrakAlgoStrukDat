def apakahKabisat(tahun):
    kabisat = False
    if (tahun % 400 == 0):
        kabisat = True
    elif tahun % 100 == 0:
        kabisat = False
    elif tahun % 4 == 0:
        kabisat = True

    if kabisat:
        print('itu tahun kabisat')
    else:
        print('Itu bukan kabisat')


print(apakahKabisat(2020))
