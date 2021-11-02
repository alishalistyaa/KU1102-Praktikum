# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 25 Oktober 2021
# Deskripsi     : Soal Pendhuluan #2.2
#               Perulangan
#               Materi Pengenalan Komputer
#               Program yang menerima bilangan N dan menuliskan bilangan 10^x terkecil yang lebih dari N

# Kamus
# N = float
# i = integer

# Input
N = float(input('Masukkan N: '))

# Algoritma Pengolahan
x = 1 # Bilangan pangkat x
while N>=x:
    x= x*10
# Mencetak hasil ke layar
print(x)