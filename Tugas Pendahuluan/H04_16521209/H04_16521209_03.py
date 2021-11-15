# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 15 November 2021
# Deskripsi     : Soal Pendahuluan #4.2
#               Fungsi, Prosedur, dan Matriks
#               Materi Pengenalan Komputer
#               Program yang menerima masukan N dan menuliskan matriks segitiga pascal berukuran N × N.

# KAMUS 
# N : integer (input)
# i,j : integer

# Input data dan inisialisasi
N = int(input("Masukkan N: "))
# Inisialisasi Matriks kosong
A = [[0 for j in range(N)] for i in range(N)]

# Inisia;isasi angka 1 baris dan kolom pertama
for i in range(N):
    A[i][0] = 1
    A[0][i] = 1
    
# Pengolahan data (sisa matriks merupakan pertambahan atas dan kirinya)
for i in range(1, N):
    for j in range(1,N):
        A[i][j] = A[i][j-1]+A[i-1][j]

# Menampilkan hasil ke layar
for i in range(N):
    for j in range(N):
        print(A[i][j], end = " ")
    print("")