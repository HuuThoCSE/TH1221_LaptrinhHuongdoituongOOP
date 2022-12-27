import math
N = int(input("Nhập vào N phần tử:"))
while N<4 or N>10:
    N = int(input("Nhập vào N phần tử:"))
ds =[]
for i in range(N):
    print("Nhập phần tử thứ",i+1,":",end='')
    x = int(input())
    ds.append(x)
print("Danh sách vừa nhập là:",end='')
print(ds)
#Gía trị max
print("Giá trị max của danh sách là",max(ds))
#Kiem tra ds co doi xung
i = 0
f = True
while i<len(ds) and f == True:
    if ds[i]!=ds[len(ds)-i-1]:
        f = False
    i+=1
if f == True:
    print("Danh sách đối xứng")
else:
    print("Danh sách không đối xứng")
def KtraSNT(n):
    if n<1:
        return -1
    for i in range(2,n-1):
        if n%i==0:
            return -1
    return 1
tich = 1
for i in ds:
    if (KtraSNT(i)==1):
        tich *= i
print("Tích các phần tử có nội dung là số nguyên tố:",tich)
def KtrCP(n):
    if n<1:
        return 0
    i = math.sqrt(n)
    if(i*i==n):
        return 1
    else:
        return 0
tong = 0
for i in ds:
    if (KtrCP(i)==1):
        tong += i
print("Tích các phần tử có nội dung là số chính phương:",tong)




