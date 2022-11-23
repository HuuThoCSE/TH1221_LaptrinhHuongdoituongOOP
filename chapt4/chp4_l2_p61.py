ds = []

# n = int(input("Nhập số lượng phần tử: "))

# Data test
import random
n = 10
for i in range(0, n):
    ds.append(random.uniform(1, 9))

# while True:
#     x = int(input("Nhập vào một số nguyên: "))
#     if x == 0:
#         break
#     else:
#         list_int.append(x)

# In list
print(ds)

# Vi tri an so
k = int(input("Nhập vào vị trí cần xóa: "))
del ds[k]

# In list
print("Danh sách sau khi xóa là: ")
print(ds)

ds1 = []
ds2 = []

i = 0

# while i < len(ds):
#     if(ds[i]-int(ds[i])>=0.5):
#         ds1.append(ds[i])
#     else:
#         ds2.append(ds[i])
#     i+=1

for i in ds:
    if abs(i-int(i) >=0.5):
        ds1.append(i)
    else:
        ds2.append(i)

# Sử dụng list comprehension
# list1 = [i for i in ds if abs(i-int(i)) >=0.5]
# list2 = [i for i in ds if abs(i-int(i)) <0.5]

print("Danh sách 1 co phan le >= 0.5 là:")
print(ds1)
print("Danh sách 2 co phan le < 0.5 là")
print(ds2)
ds1.sort()
ds2.sort(reverse=True) # reverse -> giảm dần
i = 0

# Trộn 2 danh sách xen kẽ
dsm=[]
i=0
while i < len(ds1) and i < len(ds2):
    dsm.append(ds1[i])
    dsm.append(ds2[i])
    i+=1

if i < len(ds1):
    for j in range (i, len(ds1)):
        dsm.append(ds1[i])

if i < len(ds2):
    for j in range (i, len(ds2)):
        dsm.append(ds2[i])


print("Danh sách sau khi trộn list1 và list2: ")
for i in dsm:
    print(i, end='\t')