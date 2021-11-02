# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 1 November 2021
# Deskripsi     : Program yang menghitung sisi miring sebuah segitiga siku-siku

# Kamus
# TC = float (input)
# kodeKonversi = string (input)

# Input data dan Inisialisasi
TC = float(input("Masukkan suhu (dalam derajat calcius): "))
kodeKonversi = str(input("Masukkan kode konversi (F/R/K): "))

# Algoritma Data
if kodeKonversi == "F":
    suhu = (9/5 * TC) + 32
elif kodeKonversi == "R":
    suhu = 4/5 * TC
elif kodeKonversi == "K":
    suhu = TC + 273

print(f"Suhu akhir anda {suhu}.")