# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 1 November 2021
# Deskripsi     : Program yang menghitung kelipatan X antara a s.d b

# Kamus
# X = integer (input)
# a = integer (input)
# b = integer (input)

# Input data dan Inisialisasi

# Misalkan ada ti berisi 100
arrayhasilinput = []

# Algoritma
def BacaArray() :
    for i in range(1,5):
        inputNomor = int(input(f"Masukkan nomor ke {i}: "))
        arrayhasilinput.append(inputNomor)
    return arrayhasilinput