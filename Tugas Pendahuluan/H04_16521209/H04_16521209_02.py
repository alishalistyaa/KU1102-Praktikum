# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 15 November 2021
# Deskripsi     : Soal Pendahuluan #4.2
#               Fungsi, Prosedur, dan Matriks
#               Materi Pengenalan Komputer
#               Program yang menerima N dan M, lalu membaca matriks A berukuran N × M, dan menuliskan berapa banyak bilangan positif di dalam matriks beserta menuliskan isi matriks itu sendiri.

# KAMUS 
# M : integer (input)
# N : integer (input)
# i,j : integer
# count = integer

# Input data dan inisialisasi
N = int(input("Masukkan N: "))
M = int(input("Masukkan M: "))
count = 0

A = [[0 for j in range(M)] for i in range(N)]

# Pengolahan Data
for i in range(N):
    for j in range(M):
        A[i][j] = int(input(f"Masukkan nilai A[{i+1}][{j+1}]: "))
        if A[i][j] > 0:
            count +=1

# Menampilkan hasil ke layar
print(f"Ada {count} bilangan positif di matriks.")
for i in range(N):
    for j in range(M):
        print(A[i][j], end = " ")
    print("")


'''
# Jika harus menggunakan prosedur atau fungsi, maka:

# PROGRAM CABANG ATAU FUNGSI

def isiMatriks(N,M):
    A = [[0 for j in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            A[i][j] = int(input(f"Masukkan nilai A[{i+1}][{j+1}]: "))
    return A

def cariPositif(A, N, M):
    count = 0
    for i in range(N):
        for j in range(M):
            if A[i][j] > 0:
                count +=1
    return count

def printMatriks(A, N, M):
    for i in range(N):
        for j in range(M):
            print(A[i][j], end = " ")
        print("")

# PROGRAM UTAMA

# Input Data 
N = int(input("Masukkan N: "))
M = int(input("Masukkan M: "))

# Pengolahan untuk mengisi matriks
A = isiMatriks(N,M)

# Menampilkan matriks ke layar
print(f"Ada {cariPositif(A, N, M)} bilangan positif di matriks.")
printMatriks(A,N,M)

'''









