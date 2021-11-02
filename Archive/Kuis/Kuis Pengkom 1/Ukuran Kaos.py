
#Input
ukuran = int(input("Masukkan lebar dada anda (dalam cm): "))

#Pengolahan Data
if ukuran <= 46:
    size = "S"
elif ukuran>46 and ukuran <=48:
    size = "M"
elif ukuran>48 and ukuran <=50:
    size = "L"
elif ukuran>50 and ukuran <=52:
    size = "XL"
elif ukuran>52 and ukuran<=54:
    size = "XXL"
else:
    size = "Tidak ada ukuran kaos yang cukup."

if size == "Tidak ada ukuran kaos yang cukup.":
    print("Tidak ada ukuran kaos yang cukup.")
else:
    print(f"Ukuran kaos yang tepat adalah {size}")