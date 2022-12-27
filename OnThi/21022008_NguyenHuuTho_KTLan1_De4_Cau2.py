N = int(input("Nhập số lượng phần tử: "))
DS = []
for i in range(0, N):
    num = int(input("Nhập số nguyên: "))
    while num < 4 or num > 10:
        num = int(input("Nhập lại số nguyên: "))
    DS.append(num)

for i in range(0, N):
    print(DS[i], end=', ')
print()

print("Giá trị lớn nhất trong DS:", max(DS))
print()

flag = 0
if(DS[::-1]==DS):
    flag = 1
if(flag == 1):
    print("DS đối xứng.")
else:
    print("DS không đối xứng.")

#Ham kiem tra so ngueyn to
def Check_Songuyento(num):
    # 0 => !SNT
    flag = 1 # SNT
    if num < 2:
        return False

    for p in range(2, num):
        if num % p == 0:
            flag = 0
            break
    return True

# so nguyen to
s = 1
for i in range(0, N):
    if(Check_Songuyento(DS[i])):
        print(DS[i], end='\t')
        s *= DS[i]
print("\nTich cac so nguyen to:", s)

# Ham so chinh phuong
def Check_Sochinhphuong(num):
    i = int(math.sqrt(num))
    if(i*i == num):
        return True
    return False

# So chinh phuong
print("DS số chính phương:", end=' ')
import math
s = 0
for i in range(0, N):
    i = int(math.sqrt(DS[i])) # sqrt(num) == int(sqrt(num))
    if (i * i == DS[i]):
        print(DS[i], end='\t')
        s += DS[i]
print("\nTong:", s)