# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 1 November 2021
# Deskripsi     : Program yang menghitung kelipatan X antara a s.d b

# Kamus
# M1, M2 = Matriks

# Input data dan Inisialisasi
# Agar mempercepat, asumsikan matriks yang dipakai adalah sebagai berikut
import numpy as np
n = 3
M1 = np.random.randint(0,10,(n,n))
M2 = np.random.randint(0,10,(n,n))
print(M1)
print("====== batas ======")
print(M2)

# Algoritma
def penentuansama(M1,M2):
    for i in range(n):
        for j in range(n):
            if (M1[i][j] != M2 [i][j]):
                return 0
    return 1

if (penentuansama(M1,M2)==1):
    print("Matriks adalah identik")
else: 
    print("Matriks tidak identik.")