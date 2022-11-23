n = int(input("Nhập vào 1 số nguyên dương: "))
x = float(input("Nhập vào 1 số thực: "))
s = 1
giaithua = 1
for i in range(1, n+1):
    giaithua = giaithua * i
    s=s+(pow((-1), (i+1))*(pow(x, i)/giaithua))
print("S=", s)