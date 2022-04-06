class MhsTIF(object):
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama+',NIM'+str(self.NIM)\
           +'.Tinggaldi'+self.kotaTinggal\
           +'.UangsakuRp'+str(self.uangSaku)\
           +'tiapbulannya.'
        return s
    c0 = MhsTIF('Ika',10,'Sukoharjo', 240000)
    c1 = MhsTIF('Deni',13,'Klaten', 245000)
    c2 = MhsTIF('Budi',51,'Sragen', 230000)
    c3 = MhsTIF('Syifa',14,'Klaten', 225000)

    Daftar = [c0,c1,c2,c3]

    def cariTerkecil(Daftar):
        n = len(Daftar)
        # Anggap item pertama adalah yang terkecil
        terkecil = kumpulan[0]
        # tentukan apakah item lain lebih kecil
        for i in range(1,n):
            if kumpulan[i] < terkecil:
                terkecil = kumpulan[i]

        return terkecil #kembalikan yang terkecil
