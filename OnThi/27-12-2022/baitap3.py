hoten = " ANh  VAn Cuong "

hoten = hoten.strip()
for i in range (len(hoten)-1):
    if(hoten[i]==" " and hoten[i+1]==" "):
        hoten = hoten[:i]+hoten[i+1:]
    else:
        i+=1

print(hoten)
# Xuat ten
KhTr = hoten.rfind(" ")
ten = hoten[KhTr+1:]
print("Ten:",ten)

#Xuat ho ten
KhTr_Ho = hoten.find(" ")
ho = hoten[:KhTr_Ho]
print("Ho:", ho)

dem = 0
# for i in range(len(hoten)):
#     if(hoten[i].isnumeric()):
#         for j in dem: