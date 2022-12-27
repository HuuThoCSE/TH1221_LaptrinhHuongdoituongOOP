# 21022019_Huynh Bao Thang_Cau 2_De2_16
ds = []
n = int(input("Nhập vào số lượng phần tử n:"))
while n<4 or n>10:
    n = int(input("Nhập vào số lượng phần tử:"))
for i in range(n):
    s = int(input("Nhập vào phần tử:"))
    ds.append(s)
print("Danh sách vừa nhập là:")
print(ds)
print("Giá trị của phần tử lớn nhất trong danh sách",max(ds))
i = 0
f= True
while i<len(ds)//2 and f==True:
    if ds[i]==ds[len(ds)-i-1]:
        i+=1
    else:
        f=False
if f==True:
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

t = 1
for i in ds:
    if(KtraSNT(i)==1):
        t*=i
print("Tích các phần tử có nội dung là số nguyên tố:",t)



