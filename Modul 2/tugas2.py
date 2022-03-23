class Manusia(object):
    """class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = "lapar"
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salam, namaku ",self.nama)
    def makan(self, s):
        print("Saya baru saja makan ", s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print("Saya baru saja latihan ", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n * 2

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class manusia.
           Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan", s, "Sambil belajar.")
        self.keadaan = 'kenyang'

    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self, berubah):
        self.kotaTinggal = berubah
    def tambahUangSaku(self, plus):
        self.uangSaku += plus

class SiswaSMA(Manusia):
    """Class Siswa merupakan turunan dari class Manusia"""
    def __init__(self, nama, NISN, jur, alamat):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.nisn = NISN
        self.jurusan = jur
        self.alamat = alamat
    def __str__(self):
        a = 'Nama       : ' + str(self.nama) \
            +'NISN      : ' + str(self.nisn) \
            +'Alamat    : ' + str(self.alamat) \
            +'Jurusan   : ' + str(self.jurusan)
        print (a)
    
    def ambilNama(self):
        print (self.nama)
    def ambilNisn(self):
        print (self.nisn)
    def ambilJurusan(self):
        print (self.jurusan)
    def ambilAlamat(self):
        print (self.alamat)

