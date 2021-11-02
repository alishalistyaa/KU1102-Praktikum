N = int(input("Masukkan N: "))
M = int(input("Masukkan M: "))
a = int(input("Masukkan a: "))
b = int(input("Masukkan b: "))

# kalikan sm a
# jumlahkan atau kurangkan dgn b
count = M
list = []
x=0

while count>0:
    x+=1
    if a > M:
        count = count + b
        list.append('2')
        if (count == N):
            print("Mungkin")
            print(list[::1])
            break 
        elif count > N:
            print("tidak mungkin")
            break
    elif x > 100:
        count = count - b
        list.append('2')
        if (count == N):
            print("Mungkin")
            print(list[::1])
            break 
        elif count < N:
            print("tidak mungkin")
            break
    elif(count%a == 0):
        list.append('1')
        count = count/a
        if count == N:
                    print("Mungkin")
                    print(list[::1])
                    break
        elif (count%a)<a:
            if count > N and (count-b)%a == 0:
                count = count - b
                list.append('2')
                if count == N:
                    print("Mungkin")
                    print(list[::1])
                    break
            if (count+b)%a == 0:
                count = count +b
                list.append('2')
                if count == N:
                    print("Mungkin")
                    print(list[::1])
                    break
        else :
            pass
    else:
        if (count%a)<a:
            if (count-b)%a == 0:
                count = count - b
                list.append('2')
                if count == N:
                    print("Mungkin")
                    print(list[::1])
                    break
            if (count+b)%a == 0:
                count = count +b
                list.append('2')
                if count == N:
                    print("Mungkin")
                    print(list[::1])
                    break
