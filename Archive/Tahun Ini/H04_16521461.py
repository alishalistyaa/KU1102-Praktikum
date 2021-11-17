# NIM / Nama    : 16521461 / Crysanta Caressa
# Tanggal       : 17 November 2021
# Deskripsi     : Soal Pendahuluan 4.2
#               Fungsi, Prosedur, dan Matriks
#               Materi Pengenalan Komputer
#               Program yang menerima masukan N dan menuliskan matriks segitiga pascal berukuran N × N.

# KAMUS 
# N : integer (input)
# i,j : integer

# input user barisxkolom
N = int(input('Masukkan N: '))

#deklarasi
matriks = [[1 for j in range(N)] for i in range(N)]

#iterasi untuk memerbaharui value matriks selain baris ke-1 dan kolom ke-1
for i in range(1,N):
    for j in range(1,N):
            #mengubah indeks matriks dengan pertambahan value matriks
            matriks[i][j] = matriks[i-1][j] + matriks[i][j-1]

#menampilkan output matriks
for i in range(0,N):
    for j in range(0,N):
        print(matriks[i][j], end=' ')
    print('')