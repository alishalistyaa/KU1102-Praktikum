N = int(input("Masukkan bilangan Tuan Dip (N): "))

sum_dip = 0
sum_ric = 0
ric = 0
stop = False
for i in str(N):
    sum_dip += int(i)

while stop == False:
    ric = ric+1
    sum_ric = 0
    
    for j in str(ric):
        sum_ric += int(j)
    
    if ric > N and sum_ric == sum_dip:
        stop = True
print("Bilangan Tuan Ric adalah ", int(ric))