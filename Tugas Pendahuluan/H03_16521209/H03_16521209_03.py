# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 1 November 2021
# Deskripsi     : Soal Pendahuluan #3.3
#               Array
#               Materi Pengenalan Komputer
#               Program yang mendeteksi palindrom

# Kamus
# panjang = integer (input)
# string = string (input)
# testcase = integer

# Input Data dan Inisialisasi
panjang = int(input('Masukkan panjang string: '))
string = str(input("Masukkan string: "))
testcase = panjang // 2
palindrom = False

# Algoritma Pengolahan
for i in range(0, testcase):
    if string[i] != string[(panjang-(i+1))]:
        break
    else:
        palindrom = True

# Mencetak hasil ke layar
if palindrom == True:
    print(f"{string} adalah palindrom")
elif palindrom == False:
    print(f"{string} bukan palindrom")