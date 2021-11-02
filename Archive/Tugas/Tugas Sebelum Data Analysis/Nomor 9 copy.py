# Jika dengan asumsi program input harus rimasukkan,
# Insialisasi
NBrs1 = 3
NBrs2 = 3
NKol1 = 3
NKol2 = 3
M1 =[]
M2 = []

# Algoritma 
def masukkanmatriks(NBrs, NKol, M):
    for i in range (NBrs):
        a =[]
        for j in range(NKol):
            a.append( int(input(f"Elemen ke {i}, {j}: ")))

    for i in range(NBrs):
        for j in range(NKol):
            print(M[i][j], end=' ')
        print()

# Pelaksanaan fungsi
M1 = masukkanmatriks(NBrs1,NKol1, M1)
M2 = masukkanmatriks(NBrs1,NKol1, M2)
