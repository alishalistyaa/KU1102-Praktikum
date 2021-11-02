# Program mengecek tahun kabisat

# Kamus
# y = integer (input tahun)

# Input
y = int(input('Masukkan tahun yang akan dicek: '))

# Algoritma
if y > 0:
    if (y % 4)==0:
        if (y % 100) ==0:
            if(y % 400) == 0:
                # Jika y habis dibagi 100 dan 400.
                kabisat = True
            else:
                # Jika y habis dibagi 100 tetapi tidak habis dibagi 400
                kabisat = False
        else:
            # Jika y habis dibagi 4 namun tidak habis dibagi 100.
            kabisat = True
    else:
        # Jika y tidak habis dibagi 4
        kabisat = False

# Output (Menampilkan hasil ke layar)
if y<=0:
    print('masukan salah')
elif kabisat == True:
    print('tahun kabisat')
elif kabisat == False:
    print('bukan tahun kabisat')