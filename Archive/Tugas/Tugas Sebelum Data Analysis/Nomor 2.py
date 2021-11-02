# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 1 November 2021
# Deskripsi     : Program yang menghitung sisi miring sebuah segitiga siku-siku

# Kamus
# x = integer (input)
# y = integer (input)
# kuadran = integer (output)

# Input data dan Inisialisasi
x = int(input("Masukkan nilai x: "))
y = int(input("Masukkan nilai y: "))

# Algoritma Pengolahan

if x > 0:
    if y>0:
        kuadran = 1
    elif y<0:
        kuadran = 4
elif x <0:
    if y>0: 
            kuadran = 2
    elif y<0:
            kuadran = 3
elif x==0 or y == 0:
    kuadran = None

if kuadran == None:
    print("Kuadran tidak bisa dihitung.")
else:
    print(f"Titik P terletak di kuadran {kuadran}.")