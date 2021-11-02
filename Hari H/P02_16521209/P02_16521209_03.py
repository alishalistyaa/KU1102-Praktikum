# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 27 Oktober 2021
# Deskripsi     : Soal Praktikum #2.3
#               Perulangan
#               Materi Pengenalan Komputer
#               Program yang memberikan nilai maksimal dari jumlah suatu integer (Integer Break) 

# Kamus
# N = integer (input)
# count = integer

# Input dan Inisialisasi
N = int(input("Masukkan bilangan N: "))
count = 1

# Analisis kasus
# Untuk mencapai hasil kali terbesar, dapat dicapai dengan melihat nilai yang berada di tengah tengah
# Masalahnya adalah bisa ada lebih dari 2 bilangan yang ditambahkan
# 7 = 3 4 lebih besar dari 5 2
# 8 = 3 3 2 lebih besar dari 4 4  atau 5 3
# 9 = 3 3 3 lebih besar dari 4 4 1 atau 5 4
# 10 = 3 3 4 lebih besar dari 5 5 atau 4 4 2
# 11 = 3 3 3 2 lebih besar dari 5 6 atau 4 4 3
# Diketahui bahwa 3^sekian akan menghasilkan angka yang paling besar

# Algoritma Pengolahan
# Bilangan 2 dan 3 hanya mempunyai 2 faktor
# yaitu (satu dan satu) atau (dua dan satu)
if N == 2 or N ==3:
    N = N-1

# Looping ketika bilangan N masih lebih besar dari 4
while (N>4):
    N-=3
    count *=3

# Menghitung maksimal
maks = N * count

# Menampilkan hasil ke layar
print(f"Nilai maksimalnya adalah {maks}")
    



