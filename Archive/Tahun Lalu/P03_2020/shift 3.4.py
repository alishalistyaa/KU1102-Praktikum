# Problem Satu
a = []
b = [ ]
banyak = int(input("Masukkan banyak barang: "))
for i in range(1, banyak+1):
    a.append(int(input(f"Masukkan harga awal barang ke{i}: ")))
    diskon = (int(input(f"Masukkan besar diskon(dalam persen) barang ke{i}: ")))
    b.append(a[i]*diskon)

print(a, diskon, b)