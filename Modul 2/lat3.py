class Manusia(object):
    keadaan = 'lapar'

    def __init__(self, nama):
        self.nama = nama

    def ucapkanSalam(self):
        print("salam, namaku", self.nama)

    def makan(self, s):
        print("Saya baru saja makan", s)
        self.keadaan = 'kenyang'

    def olahraga(self, k):
        print("saya baru saja latihan", k)
        self.keadaan = 'Laper'

    def mengalikanDenganDua(self, n):
        return n*2


p1 = Manusia('Syifaul')
p1.ucapkanSalam()
