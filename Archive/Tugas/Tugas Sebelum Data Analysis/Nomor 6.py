# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 1 November 2021
# Deskripsi     : Program yang menghitung kelipatan X antara a s.d b

# Kamus
# TI = array
# count = integer

# Input data dan Inisialisasi
import random
TI = random.sample(range(-999,1000), 100)
print(TI)
count = 0

# Misalkan ada ti berisi 100

# Algoritma
for i in TI:
    if i <0:
        print("Tidak semua elemen array positif.")
        break
    if i >=0:
        count +=1
if count ==100:
    print("Semua elemen array positif.")