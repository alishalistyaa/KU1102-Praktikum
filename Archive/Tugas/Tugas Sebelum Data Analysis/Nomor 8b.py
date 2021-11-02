# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 1 November 2021
# Deskripsi     : Program yang menentukan apakah kedua array identik atau tidak

# Kamus
# BacaArray = function
# T1,T2 = Array
# penentuansama = function
# apakahsama = char


# Input data dan Inisialisasi
T1 = []
T2 = []

def BacaArray(n) :
    print(f"Silahkan input untuk array.")
    for i in range(1,101):
        inputNomor = int(input(f"Masukkan integer di array ke {i}: "))
        n.append(inputNomor)
    return n

T1 = BacaArray(T1)
T2 = BacaArray(T2)
print(T1)
print(T2)

apakahsama = 1

def penentuansama():
    for i in range(len(T1)):
        if T1[i] != T2[i]:
            return 0
    return 1

# Mencetak hasil ke layar
if penentuansama() == 0:
    print("Array Tidak sama")
elif penentuansama() ==1:
    print("Array sama")
        
