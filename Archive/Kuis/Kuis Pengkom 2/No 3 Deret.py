# Program kalkulasi deret

# Kamus
# a = integer (input)
# b = integer (input)
# n = integer (input)

# Input
a = float(input('Masukkan a: '))
b = float(input('Masukkan b: '))
n = int(input('Masukkan n: '))

# Adalah jumlah bilangan untuk keep track
count = 0

if n > 0: #Untuk make sure bahwa n > 0
    for i in range(1,n+1):
        x = int(input(f'Masukkan x ke-{i}: '))
        count += a*(x**i) +b
        # Print hasil deret ke layar
    print(f'Jumlah deret anda adalah {count}.')
else: # Jika n <= 0, progtam tidak berjalan
    print('Input n tidak valid')