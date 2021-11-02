# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 1 November 2021
# Deskripsi     : Program yang menghitung sisi miring sebuah segitiga siku-siku

# Kamus
# a = float (input)
# b = float (input)
# c = float (output)

# Input data dan Inisialisasi
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))

# Algoritma Pengolahan
def sisimiring(a,b):
    c = ((a**2) + (b**2))**(1/2)
    return c

print(f"sisi miring c adalah {sisimiring(a,b)}.")