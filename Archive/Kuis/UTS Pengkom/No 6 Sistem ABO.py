# Program
# Program menggolongkan golongan darah

# Kamus
# Ix = string
# Iy = string
# Gol = string

# Input
Ix  = str(input("Alel yang diwariskan dari ibu: "))
Iy = str(input("Alel yang diwariskan oleh ayah: "))

# Pengolahan data
if Ix == "IA":
    if Iy == "IA":
        Gol = "A"
    elif Iy == "IB":
        Gol = "AB"
    elif Iy == "IO":
        Gol = "A"
elif Ix =="IB":
    if Iy == "IA":
        Gol = "AB"
    elif Iy == "IB":
        Gol = "B"
    elif Iy == "IO":
        Gol = "B"
elif Ix == "O":
    if Iy == "IA":
        Gol = "A"
    elif Iy == "IB":
        Gol = "B"
    elif Iy == "IO":
        Gol = "O"
else:
    Gol = "None"

# Mencetak ke layar
if Gol == "None":
    print("Input alel tidak valid.")
else:
    print(f"Golongan darah anak adalah {Gol}")