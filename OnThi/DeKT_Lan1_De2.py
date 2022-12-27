N = int(input('Nhập số nguyên dương chẵn: '))
while N % 2 != 0 or N >= 10 or N <0:
    N = int(input('Nhập số nguyên dương chẵn: '))

for i in range(0, N):
    for j in range(0, N):
        print("*", end="\t")
    print()