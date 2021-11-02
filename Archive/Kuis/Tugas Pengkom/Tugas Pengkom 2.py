# Program
# Mencari hambatan total suatu sistem

# KAMUS
# r1, r2, r3 = float (input)
# rt = float (output)

count = 0
for i in range(1,4):
    r = float(input(f'Masukkan nilai hambatan ke-{i}: '))
    if r < 0:
        print('Hambatan total tidak bisa dihitung.')
        break
    count += r

# Mencetak hasil ke layar
if r >= 0:
    print(f"Hambatan totalnya adalah {count}.")