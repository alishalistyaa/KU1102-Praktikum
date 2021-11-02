# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 06 Oktober 2021
# Deskripsi     : Soal Pendhuluan #2.2
#               Perulangan
#               Materi Pengenalan Komputer
#               Gunting Batu Kertas

'''

ronde = int(input("Masukkan jumlah ronde: "))
countMor = 0
countVin = 0

for i in range(0, ronde):
    mor = str(input(f'Masukkan gerakan Tuan Mor ke-{i+1}: '))
    vin = str(input(f'Masukkan gerakan Tuan Vin ke-{i+1}: '))
    if mor == 'R':
        if vin == 'S':
            countMor+=1
        elif vin == 'P':
            countVin +=1
        elif vin == mor:
            pass
    elif mor == 'S':
        if vin == 'P':
            countMor +=1
        elif vin == 'R':
            countVin +=1
        elif vin == mor:
            pass
    elif mor == 'P':
        if vin == 'R':
            countMor +=1
        elif vin == 'S':
            countVin +=1
        elif vin == mor:
            pass
if countMor > countVin:
    print('Pemenangnya adalah Tuan Mor.')
elif countMor < countVin:
    print('Pemenangnya adalah Tuan Vin.')
elif countMor == countVin:
    print('Permainan berakhir seri.')
    
'''

# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 06 Oktober 2021
# Deskripsi     : Soal Praktikum #2.2
#               Perulangan
#               Materi Pengenalan Komputer
#               Basis Angka
'''
n = int(input('Masukkan nilai N: '))
k = int(input('Masukkan nilai K: '))
count = 0

for i in range(1,n+1):
    digit = int(input(f'Masukkan digit ke-{i}: '))
    count = count + digit*(k**(n-i))

print(f'Bilangan dalam basis 10 adalah {count}.')
'''

# NIM / Nama    : 16521209 / Alisha Listya Wardhani
# Tanggal       : 06 Oktober 2021
# Deskripsi     : Soal Praktikum #2.2
#               Perulangan
#               Materi Pengenalan Komputer
#               Basis Angka
'''
x = int(input('Masukkan X: '))
n = 2
p = 0
bilcan = 11
testrun = True

while testrun:
    if len(str(x)) == 1:
        testrun = False
        bilcan = x
    else:
        for i in range(1,10):
                angkacantik  = i*bilcan
                i+=1
                if angkacantik%x == 0:
                    testrun = False
        bilcan = bilcan + 10**n
        n+=1
print(f'Bilangan cantik anda adalah {angkacantik}')

'''

x = int(input('Masukkan X: '))

bil_can = 1

flag = True
while flag:
    strBil = str(bil_can)
    if x % 2 != 0 and x % 5 != 0 and bil_can % x == 0:
        if strBil == len(strBil) * str(bil_can  % 10):
            flag = False
            bil_can -= 1
    bil_can += 1

print(f'Bilangan cantik terkecil yang habis dibagi {x} ialah {bil_can}')