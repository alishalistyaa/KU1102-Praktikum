# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 1 November 2021
# Deskripsi     : Program yang menghitung kelipatan X antara a s.d b

# Kamus
# M : matriks of integer
# NBrs, NKol : int(ukuran matriks)
# i, j : int(indeks)

# ALGORITMA

# deklarasi matriks
jumlah = 3
NBrs = jumlah
NKol = jumlah
M = [[0 for j in range(NKol)] for i in range(NBrs)]

# Mengisi matriks ukuran
for i in range (NBrs):
    for j in range(NKol):
        M[i][j] = int(input(f"Elemen ke {i}, {j}: "))

for i in range(NBrs):
    for j in range(NKol):
        print(str(M[i][j])+" ", end=' ')
    print()

# Cek Matriks
cek = False
for i in range(1,NKol):
    for j in range(0,i):
        if (M[i][j] != 0):
            cek = False
        else:
            cek = True

if NBrs != NKol:
    print("Bukan matriks segitiga")
if cek == True:
    print("Matriks segitiga atas")
else:
    print("Bukan matriks segitiga")