
# Input
a = int(input("Masukkan suku pertama (a): "))
b = int(input("Masukkan selisih antar suku (b): "))
n = int(input("Masukkan banyaknya suku: "))
sum = 0
i = 1

# Pengolahan Data
for i in range(1, n+1):
    sum = sum + ( a + ((i-1)*b) )
    i=+1

# Output
print(f"S({n}) = {sum}.")
