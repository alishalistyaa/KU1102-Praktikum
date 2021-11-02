# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 25 Oktober 2021
# Deskripsi     : Soal Pendhuluan #2.3
#               Perulangan
#               Materi Pengenalan Komputer
#               Program yang menerima bilangan X dan apakah X adalah bilangan prima

# Kamus
# x = integer

# Input
X = int(input("Masukkan X: "))

# Algoritma Pengolahan
i = 2
while i <= X:
    if i < X:
        if X % i == 0:
            print(f'{X} bukan bilangan prima')
            # Sesaat setelah menemukan faktornya, while loop berhenti
            break 
        # Kalo i masih kurang dari X, i ditambah satu
        i += 1 
    elif X == i:
        print(f'{X} adalah bilangan prima')
        break
    
    
# Siapatahu inputnya bilangan negatif...
if X < 0:
    print(f'{X} adalah bilangan negatif')