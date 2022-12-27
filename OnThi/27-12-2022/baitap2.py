a = 4.5
b = 4.3
c = 1.3
d = 5.6
print(min(a, b, c, d))

# Giai thừa của 1 số nguyên
s = 1
n = 5
for i in range(2, n+1):
    s *= i
print(s)
print()

# Ước số của 1 số nguyên
n = 8
print(f"Ước số của {n}: ")
for i in range(1, n+1):
    if n%i==0:
        print(i)
print()
# Tổng các bội số (từ nhỏ đến lớn)
n = 24
s = 0

i = 1
while s < n:
    if i%n==0:
        s += i
    i+=1
print(f"Tổng các bội số (từ nhỏ đến lớn) của {n}:", s)