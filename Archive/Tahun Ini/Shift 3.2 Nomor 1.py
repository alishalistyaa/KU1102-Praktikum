N = int(input("Masukkan bilangan Tuan Dip (N): "))
ric = N 
jumlahdip = 0
jumlahric = 0
stop = False

# Menghitung jumlah
for i in str(N):
    jumlahdip += int(i)

while stop == False:
    ric = ric+1
    jumlahric = 0
    
    for j in str(ric):
        jumlahric += int(j)
    
    if ric > N and jumlahric == jumlahdip:
        stop = True


print("Bilangan Tuan Ric adalah", int(ric))