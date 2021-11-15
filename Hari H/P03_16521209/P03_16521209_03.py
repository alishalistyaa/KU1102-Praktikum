# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 3 November 2021
# Deskripsi     : Soal Praktikum #3.3
#               Array
#               Materi Pengenalan Komputer
#               Program yang mencari suatu kata dalam input string

# Kamus
# count = integer
# stringsatu = integer (input)
# stringdua = integer (input)
# inputsatu = string (input), treated sebagai array
# inputdua = string (input), treated sebagai array

# Inisialisasi count
count = 0

# Input Data
# yang dicari
stringsatu = int(input("Masukkan panjang string 1: "))
inputsatu = str(input("Masukkan string 1: "))
# string semuanya
stringdua = int(input("Masukkan panjang string 2: "))
inputdua = str(input("Masukkan string 2: "))

# Pengolahan data
for i in range(stringdua):
    for j in range(stringsatu):
        # Kalau sama
        if inputdua[i] == inputsatu[j]:
            # Kalau ketemu sampe akhir kata yang dicari
            if j == stringsatu-1:
                count += 1

# Menampilkan hasil ke layar
print(f"String 1 muncul sebanyak {count} kali.")


# semangat kak meriksanya dan menghadapi dikra:(