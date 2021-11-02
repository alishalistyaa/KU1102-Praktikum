# Program
# Program mengitung indeks

# Kamus
# NA = integer
# NB = integer
# NC = integer
# ND = integer
# NE = integer
# NR = Float

# Input
NA = int(input("Masukkan banyaknya SKS mata kuliah yang mendapat nilai A: "))
NB = int(input("Masukkan banyaknya SKS mata kuliah yang mendapat nilai B: "))
NC = int(input("Masukkan banyaknya SKS mata kuliah yang mendapat nilai C: "))
ND = int(input("Masukkan banyaknya SKS mata kuliah yang mendapat nilai D: "))
NE = int(input("Masukkan banyaknya SKS mata kuliah yang mendapat nilai E: "))

# Algoritma Pengolahan
NR = ((NA*4)+(NB*3)+(NC*2)+(ND*1))/(NA+NB+NC+ND)


# Cetak hasil ke layar
print(f"Nilai rata-rata kamu adalah: {NR}.")
