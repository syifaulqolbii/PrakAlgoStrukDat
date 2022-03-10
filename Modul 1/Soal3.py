def jumlahHurufVokal(x):
    vokal = " AIUEOaiueo"
    jumVokal = ""

    for character in x:
        if character in vokal:
            jumVokal += character
    return len(x), len(jumVokal)


print(jumlahHurufVokal('syifaul'))


def jumlahHurufKonsonan(x):
    vokal = " AIUEOaiueo"
    jumKonsonan = ""

    for character in x:
        if character not in vokal:
            jumKonsonan += character
    return len(x), len(jumKonsonan)


print(jumlahHurufKonsonan('syifaul'))
