# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 17 November 2021
# Deskripsi     : Soal Praktikum #4.2
#               Fungsi, Prosedur, dan Matriks
#               Materi Pengenalan Komputer
#               Program yang memecahkan permasalahan permutasi

# KAMUS
# panjang : integer(input)
# kata : string (input)
# pembilang, penyebut, hasil : integer
# jumlahhuruf : integer
# unique, listkata : list

# PROGRAM FUNGSI
def faktorial(x):
    # KAMUS LOKAL
    # count, x = integer
    count = x
    while x>1:
        x -= 1
        count *= x
    return count


# PROGRAM UTAMA
# Input data dan Inisialisasi
panjang = int(input("Masukkan panjang string: "))
kata = str(input("Masukkan string: "))

# Pembilang dan Penyebut
pembilang = faktorial(panjang)

# Pengolahan data untuk penyebut
penyebut = 1
listkata = list(kata)
unique = [0 for i in range(panjang)]

# Ingin menemukan berapa huruf berulang dan cari faktorialnya
for i in range(panjang):
    jumlahhuruf = 0
    for j in range(panjang):
        if listkata[j] == listkata[i]:
            jumlahhuruf += 1
        else: 
            pass
    if jumlahhuruf > 1 and (listkata[i] not in unique):
        penyebut *= faktorial(jumlahhuruf)
        unique[i] = listkata[i]

# Hasil permutasi
hasil = int(pembilang / penyebut)

# Menampilkan hasil ke layar
print(f"String tersebut dapat membentuk {hasil} kata berbeda")
