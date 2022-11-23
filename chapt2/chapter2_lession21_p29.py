n = int(input("Nhập vào 1 số nguyên dương: "))
i = 2
print(n, end='= ')
while (n > 1):
    if (n % i == 0):
        n = int(n / i)
        print(i, end=' ')
    else:
        i = i + 1
