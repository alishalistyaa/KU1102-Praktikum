# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 1 November 2021
# Deskripsi     : Program mengurutkan angka yang diinput dari angka terbesar

# Kamus
# a, b, c = integer (input)

# Input data dan Inisialisasi
a = int(input("Masukkan angka a: "))
b = int(input("Masukkan angka b: "))
c = int(input("Masukkan angka c: "))

#Mencetak hasil ke layar
if a > b and a > c:
    if b > c:
        print(a,b,c)
    elif c > b:
        print(a,c,b)
elif b > a and b >c:
    if a > c:
        print(b,a,c)
    elif c > a:
        print(b,c,a)
elif c > a and c > b:
    if a > b:
        print(c,a,b)
    elif b > a:
        print(c,b,a)