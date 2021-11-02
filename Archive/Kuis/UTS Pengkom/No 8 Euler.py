# Program perhitungan tahun

# Input
x = int(input("Banyaknya tahun: "))
k = 0.015
Po = 1200000
e = 0
f = 1

# Pengolahan
for i in range(0, 101):
    if i == 0:
        e += 1
    elif i > 0:
        f *= i
        e += 1/(f)

for t in range(1,x+1):
    Ppert = Po*(e**(k*t))
    Pfinal = round(Ppert/1000000,2)
    print(f"Tahun ke-{t}: {Pfinal} juta")  