# Program menghitung jarak tempuh benda

# Kamus
# a = integer (konstanta)
# v = integer (konstan)
# t = integer (input)
# s0 = integer (input)
# st = integer (output)

# Input
s0 = float(input('Masukkan jarak awal benda: '))
t = float(input("Masukkan waktu tempuh : "))
a = 10**(-2)
v = 10

# Algoritma
st = (1/2*a*(t**2))+(v*t)+s0

# Menuliskan ke layar
print(f'Jarak tempuh adalah {st}.')