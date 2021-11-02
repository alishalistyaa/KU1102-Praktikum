# KAMUS
# N = integer

# Input
suhuAir = int(input("Masukkan suhu air: "))

# Algoritma Pengolahan 
# dan mencetak hasil ke layar
if suhuAir<=0:
    print('beku')
elif suhuAir > 0 and suhuAir<100:
    print('cair')
else:
    print("uap")