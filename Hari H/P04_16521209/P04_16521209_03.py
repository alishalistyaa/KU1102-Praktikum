# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 17 November 2021
# Deskripsi     : Soal Praktikum #4.3
#               Fungsi, Prosedur, dan Matriks
#               Materi Pengenalan Komputer
#               Program yang memecahkan permasalahan permutasi

# KAMUS
# baris, kolom, count : integer
# A : Matriks

# Pengolahan data
# Inisialisasi dan input data
baris = int(input("Masukkan brs: "))
kolom = int(input("Masukkan klm: "))
count = 0

A = [[0 for j in range(kolom)] for i in range(baris)]

# Pengolahan Data
for i in range(baris):
    for j in range(kolom):
        A[i][j] = int(input(f"Masukkan nilai petak baris {i+1} kolom {j+1}: "))

for i in range(baris):
    for j in range(kolom):
        # Jika pulau berada di pinggir matriks maka:
        if j == 0 and (A[i][j] == 1):
            count +=1
        if i == 0 and (A[i][j] == 1):
            count +=1

        # Jika pulau berada di tengah matriks tapi dikelilingi laut
        if (j >0):
            if A[i][j] == 1 and A[i][j-1] == 0:
                count +=1
            if (j<baris-1):
                if A[i][j] == 1 and A[i][j+1] == 0:
                    count+=1
        if (i>0):
            if A[i][j] == 1 and A[i-1][j] == 0:
                count += 1
            if (i<baris-1):
                if A[i][j] == 1 and A[i+1][j] == 0:
                    count+=1
        
        # Jika pulau dipinggir matriks
        if i == baris-1 and (A[i][j] == 1):
            count+=1
        if j == baris-1 and (A[i][j] == 1):
            count+=1

# Menampilkan hasil ke layar
print(f"Keliling pulau tersebut adalah {count}.")