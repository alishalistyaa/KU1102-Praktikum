# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 3 November 2021
# Deskripsi     : Soal Praktikum #3.1
#               Array
#               Materi Pengenalan Komputer
#               Program yang menghitung jumlah huruf konsonan dan huruf vokal pada suatu kalimat

# Kamus
# N : integer (input)
# kalimat : string (input)
# vokal, konsonan, spasi = integer (keep track)

# Input Data
N = int(input("Masukkan N: "))
kalimat = str(input("Masukkan string: "))
# Inisialisasi
vokal = 0
konsonan = 0
spasi = 0

# Pengolahan data
# Karena takut gaboleh langsung checking di string,
'''
for i in kalimat:
    if i == "a" or i == "i" or i == "u" or i == "e" or i =="o":
        vokal += 1
    elif i == ' ':
        spasi += 1
    else:
        konsonan +=1
'''

# Pengolahan data lagi
for i in range(N):
    if kalimat[i] == "a" or kalimat[i] == "i" or kalimat[i] == "u" or kalimat[i] == "e" or kalimat[i] == "o":
        vokal += 1
    elif kalimat[i] == " ":
        spasi += 1
    else:
        konsonan +=1


# Menayangkan hasil ke layar
print(f"Terdapat {vokal} huruf vokal dan {konsonan} huruf konsonan.")