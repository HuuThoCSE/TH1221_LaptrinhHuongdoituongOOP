#21022010_LeNguyenQuangBinh_CAU2_DE2_06
import math
n=int(input("Nhập số nguyên N: "))

while n!=0:
    if n in range(4,11):
        a.append(n)
    n = int(input("Nhập số nguyên N: "))
print("Danh sách vừa nhập là:\n",a)
print("Giá trị lớn nhất trong danh sách là: ",max(a))
b=a
b.reverse()
if b==a:
    print("\nDanh sách đối xứng!")
else: print("\nDanh sách không đối xứng!")
tich=1
a=[]
for i in a:
    check=True
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            check=False
    if check:
        tich*=i
print("Tích của các số nguyên tố có trong danh sách= ",tich)