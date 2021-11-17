# Problem 1
'''
N = int(input("Masukkan nilai N: "))
A = [[ 0 for i in range(N)] for j in range(N)]
amangak = True

for i in range(N):
    for j in range(N):
        A[i][j] = str(input(f"Masukkan elemen baris {i+1} kolom {j+1}: "))

for i in range(N):
    for j in range(N):
        if A[i][j] =='R':
            for k in range(N):
                if A[i][k] == 'B':
                    amangak = False
                    break
            for l in range(N):
                if A[l][j] == 'B':
                    amangak = False
                    break
        
if amangak == False:
    print("Ratu tidak aman.")
else:
    print("Ratu aman")
'''

# Problem 2
pesan = str(input("Masukkan pesan awal: "))
N = int(input("Masukkan nilai N: "))
abjad = 'abcdefghijklmnopqrstuvwxyz'
listpesan = list(pesan)
listabjad = list(abjad)

def ubahkata(N):
    for i in range(len(listabjad)):
        if listpesan[count] == listabjad[i]:
            if i+N < len(listabjad):
                listpesan[count] = listabjad[i+N]
                break
            elif i+N > len(listabjad):
                listpesan[count] = listabjad[i+N-26]
                break

for count in range(len(listpesan)):
    ubahkata(N)
print(listpesan)