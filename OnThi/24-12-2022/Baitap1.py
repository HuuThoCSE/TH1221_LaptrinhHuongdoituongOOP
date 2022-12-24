N = int(input('Nhập số nguyên dương chẵn: '))
while N % 2 != 0 or N >= 10 or N <0:
    N = int(input('Nhập số nguyên dương chẵn: '))

# Tam giác vuông cân
print("Vẽ tam giác vuông cân: ")
for i in range(0, N):
    for j in range(0, i+1):
        print("*", end=" ")
    print()
print()
n=N

print("Vẽ tam giác sao vuông cân: ")
for i in range(n+1, 0, -1):
    for j in range(1, i):
        print("*", end=" ")
    print()
print()

print("Vẽ tam giác đều: ")
for i in range(1, n+1):
    for j in range(1, n+1-i):
        print("", end=" ")
    for k in range(1, i+1):
        print("*", end=" ")
    print()
print()

print("Vẽ tam giác đều: ")
for i in range(1, n+1):
    for j in range(1, i+1):
        print("", end=" ");
    for j in range(1, n+2-i):
        print("*", end=" ")
    print()

print("Vẽ tam giác cân ngược: ")
for i in range(0, n):
    for j in range(0, i):
        print("", end=" ")
    for j in range(i, n):
        print(" *", end="")
    print()
print()

