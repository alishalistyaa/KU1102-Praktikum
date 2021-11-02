# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 1 November 2021
# Deskripsi     : Program yang menghitung maksimum, minimum dari sebuah array

# Kamus
# TI = array
# initialmin, initialmax = integer
# pilihan = integer (input)


# Random number untuk T1
import random
TI = random.sample(range(-999,1000), 100)
print(TI)

# Input Data dan Insisialisasi
print('''
============== PILIHAN ================
Pilihan 0: Menuliskan nilai maksimum dan minimum
Pilihan 1: Menuliskan nilai maksimum saja
Pilihan 2: Menuliskan nilai minimum saja
=======================================
''')
pilihan = int(input("Masukkan pilihan anda (0/1/2): "))
initialmin = TI[0]
initialmax = TI[0]

# Algoritma pengolahan dan cetak hasil ke layar
if pilihan == 0:
    for i in TI:
        if i > initialmax:
            initialmax = i
        if i < initialmin:
            initialmin = i
        else:
            pass
    print(f"Nilai maksimumnya {initialmax} dan minimumnya {initialmin}.")
elif pilihan == 1:
    for i in TI:
        if i > initialmax:
            initialmax = i
        else:
            pass
    print(f"Nilai maksimumnya {initialmax}.")
elif pilihan == 2:
    for i in TI:
        if i < initialmin:
            initialmin = i
        else:
            pass
    print(f"Nilai maksimumnya {initialmin}.")