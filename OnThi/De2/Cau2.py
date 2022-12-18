N = int(input("Nhập vào số nguyên dương (2-9): "))

while N < 2 or N > 9:
    N = int(input("Nhập lại số nguyên dương (2-9): "))

# Bội số chẵn và nhỏ hơn 100 theo thứ tự giảm dần...
for i in range(99, -1, -1):
    if i%N==0 and i%2==0:
       print(i)