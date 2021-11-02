# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 27 Oktober 2021
# Deskripsi     : Soal Praktikum #2.2
#               Perulangan
#               Materi Pengenalan Komputer
#               Program yang menghitung berapa jumlah ember

# Kamus
# x = integer (input)
# y = integer (input)
# z = integer (input)
# x1 = integer (output)
# y1 = integer (output)
# z1 = integer 

# Input dan inisialiasi
x = int(input("Masukkan x: "))
y = int(input("Masukkan y: "))
z = int(input("Masukkan z: "))

# Inisialiasi keep track ember yang dibutuhkan
z1 = z # saya manipulasi z pada variabel z1 agar z asli tidak berubah
x1 = 0
y1 = 0
walk = True

def check():
    if z1 == 0:
        print(f"{x1} kali ember x, {y1} kali ember y")
    elif z1 > 0:
        pass
    elif z1 < 0:
        walk = False

# Pengolahan
while z1 > 0 and walk:
    if z1 % x != 0:
        z1 -= y
        y1 += 1
        check()
    elif z1 % y !=0:
        z1 -= x
        x1 += 1
        check()
    elif z1 % x == 0:
        z1 -= x
        x1 += 1
        check()
    elif y1 % x == 0:
        z1 -= y
        y1 += 1
        check()

if z1<0:
    print("Tidak mungkin")
