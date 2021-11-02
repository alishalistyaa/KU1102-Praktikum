# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 1 November 2021
# Deskripsi     : Program yang menghitung kelipatan X antara a s.d b

# Kamus
# X = integer (input)
# a = integer (input)
# b = integer (input)
# count = integer

# Input data dan Inisialisasi
X = int(input("Masukkan kelipatan: "))
a = int(input("Masukkan angka a: "))
b = int(input("Masukkan angka b: "))
count = 0

# Algoritma
for i in range(a+1, b):
    if i % X == 0:
        count+=1
    else:
        pass
# Mencetak hasil ke layar
print(f"Ada {count} bilangan kelipatan {X} antara {a} dan {b}.")