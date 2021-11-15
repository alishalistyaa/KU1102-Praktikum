# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 3 November 2021
# Deskripsi     : Soal Praktikum #3.2
#               Array
#               Materi Pengenalan Komputer
#               Program yang menebak keaddan akhir rangkaian lampu berdasarkan input tuan Kil

# Kamus
# lampu = integer (input)
# tombol = integer (input)
# hasil = array
# pencet = integer (input)
# muncullah = string (output)

# Input Data
lampu = int(input("Masukkan banyak lampu: "))
tombol = int(input("Masukkan berapa kali Tuan Kil menekan tombol: "))
# Inisialisasi
hasil = [0 for k in range (0, lampu)]

for i in range(1, tombol+1):
    pencet = int(input(f"Tombol yang ditekan ke {i}: "))
    # Agar tombol yang dipencet dan teman teman di kanan kirinya ikutan,
    for j in range(pencet-2, pencet+1):
        # Kalau negatif biar indeks ga mempengaruhi
        if j < 0:
            pass
        # Kalau indeks nya sama, out of range
        elif j == lampu: 
            pass
        # Kalau 0 jadi 1
        elif hasil[j]==0:
            hasil[j]=1
        # Kalau 1 jadi 0
        elif hasil[j]==1:
            hasil[j]=0

# Karena takut gaboleh pake.join atau map
muncullah =''
for digit in hasil:
    muncullah += str(digit)

# Menampilkan hasil ke layar
print(f"Keadaan akhir rangkaian lampu adalah {muncullah}.")