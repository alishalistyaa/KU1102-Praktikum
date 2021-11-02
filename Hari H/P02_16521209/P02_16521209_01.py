# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 27 Oktober 2021
# Deskripsi     : Soal Praktikum #2.1
#               Perulangan
#               Materi Pengenalan Komputer
#               Program yang mengubah N menjadi satu

# Kamus
# N = integer

# Input dan inisialisasi
N = int(input("Masukkan bilangan N: "))
count = 0 # untuk mentrack berapa langkah yang sudah dilewati

# Algoritma Pengolahan
while N > 1:
    if N % 2 == 1:
        N -=1
        count +=1
    elif N % 2 == 0:
        N = N/2
        count +=1

# Menampilkan hasil ke layar
print(f"Banyak langkah yang diperlukan adalah {count}.")
