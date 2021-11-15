# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 1 November 2021
# Deskripsi     : Soal Pendahuluan #3.2
#               Array
#               Materi Pengenalan Komputer
#               Program yang menentukan anagram

# Kamus
# a,b = array
# count = integer 
# i, j, k, l = integer

# Inisialisasi
a = []
b = []
count = 0

# Input data
A = int(input("Masukkan banyaknya elemen A: "))
for i in range(1, A+1):
    a.append(int(input(f"Masukkan elemen A ke-{i}: ")))
B = int(input("Masukkan banyaknya elemen B: "))
for j in range(1, B+1):
    b.append(int(input(f"Masukkan elemen A ke-{j}: ")))

# Algoritma Pengolahan
for k in a:
    for l in b:
        if k == l:
            count +=1
        elif k != l:
            pass

# Mencetak hasil ke layar
if len(a) == len(b) and count == len(a):
    print("B adalah anagram dari A")
else:
    print("B bukan anagram dari A.")