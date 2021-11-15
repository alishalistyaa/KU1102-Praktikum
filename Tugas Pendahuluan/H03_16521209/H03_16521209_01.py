# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 1 November 2021
# Deskripsi     : Soal Pendahuluan #3.1
#               Array
#               Materi Pengenalan Komputer
#               Program yang menerima N buah bilangan dan menuliskan kembali bilangan tersebut, namun terbalik.

# Kamus
# N = integer
# x = float
# i = integer
# daftarBilangan = list

# Input data dan Inisialisasi
N = int(input("Masukkan N: "))
daftarBilangan = []
j = -1

# Algoritma Pengolahan
for i in range(1,N+1):
    x = int(input())
    daftarBilangan.append(x)

# Mencetak ke layar
print('Hasil dibalik:')
while j >= -1*N:
    print(daftarBilangan[j])
    j -= 1