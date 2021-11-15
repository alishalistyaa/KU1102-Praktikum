# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 15 November 2021
# Deskripsi     : Soal Pendahuluan #4.1
#               Fungsi, Prosedur, dan Matriks
#               Materi Pengenalan Komputer
#               Program yang menerima A dan B, lalu menuliskan semua nilai darif(A),f(A+1),...,f(B)

# KAMUS 
# A : integer (input)
# B : integer (input)
# i : integer
# count = integer

# PROGRAM FUNGSI
def hitung(x):
    # KAMUS LOKAL 
    # pers : integer

    # ALGORITMA
    pers = (x**2)-(2*x)+5
    return pers

# PROGRAM UTAMA
# Inisialisasi dan Input Data
A = int(input("Masukkan A: "))
B = int(input("Masukkan B: "))

# Looping dari f(A) sampai f(B)
for i in range(A, B+1):
    # Menampilkan hasil ke layar
    print(f"f({i}) = {hitung(i)}")


