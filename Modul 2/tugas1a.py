class Pesan(object):
    """Sebuah class bernama Pesan.
       Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('kalimatku mempunyai', len(self.teks), 'karakter.')
    def perbarui(self, stringBaru):
        self.teks = stringBaru
    def apakahTerkandung(self, a):
        if a in self.teks:
            return True
        else :
            return False
    def hitungKonsonan(self):         
        k = self.teks
        vokal = 'aiueoAIUEO'
        jum = 0
        for i in k :
            if i.lower() not in vokal:
                jum += 1
        return jum
    def hitungVokal(self):
        vocal = 0
        z = self.teks
        huruf = "aiueoAIUEO"
        for i in z:
            if i in huruf:
                vocal += 1
        return vocal

