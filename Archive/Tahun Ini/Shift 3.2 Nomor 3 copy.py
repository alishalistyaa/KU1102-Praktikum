k = int(input("Masukkan kelipatan: "))
n = int(input("Banyak suku yang diinginkan: "))
m = k

# Pengolahan
for i in range(1, n+1):
    print(m, end=' ')
    m -= 1
    stop = False
    while i%k == 0 and stop == False:
        m = k+i
        stop = True