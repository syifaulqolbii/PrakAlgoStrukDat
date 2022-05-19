# ================Latihan================
import re
s = 'Sebuah contoh kata:teh!!'
cocok = re.findall(r'kata:\w\w\w', s)

if cocok:
    print('menemukan', cocok)
else:
    print('tidak menemukan')

# ================Latihan================
s = 'Sebuah contoh kata:batagor!!'
cocok = re.findall(r'kata:\w\w\w', s)

if cocok:
    print('menemukan', cocok)
else:
    print('tidak menemukan')

s = 'Sebuah contoh kata:es teh!!'
cocok = re.findall(r'kata:\w\w\w', s)

if cocok:
    print('menemukan', cocok)
else:
    print('tidak menemukan')

# ==============Latihan 2====================
# Dua baris ini mencari pola ’eee’ distring ’teeeh’.
# Seluruh pola harus cocok,tapi itu bisa muncul dimana saja.
# Jika berhasil, \texttt{cocok} adalah daftar semua teks yang cocok.
cocok1 = re.findall(r'eee', 'teeeh')  # => cocok == [’eee’]
cocok2 = re.findall(r'ehs', 'teeeh')  # => cocok == []

# .=semuakarakterkecuali\n
cocok3 = re.findall(r'..h', 'teeeh')  # => cocok == ['eeh']

# \d = karakterangka,\w = karakter huruf atau angka
# => cocok == [’123’,’201’]
cocok4 = re.findall(r'\d\d\d', 't123h di 2019 bulan 02')
# => cocok == [’def’,’tgh’]
cocok5 = re.findall(r'\w\w\w', '@@a*bc#def*tghh!!')

print(cocok1, cocok2, cocok3, cocok4, cocok5)
