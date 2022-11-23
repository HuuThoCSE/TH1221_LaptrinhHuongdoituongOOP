import string
a=input("Nhập 1 chuỗi bất kì: ")
found= False
b=a[0]
temp=0
i=1
while len(b)< len(a)//2 and found==False:
    temp = len(a)//len(b)
    if  b * temp== a:
        found = True
    else:
        b = b + a[i]
    i+=1
if found==True:
    print("Chuỗi trên được tạo từ: ", b)
else:
    print("Chuỗi trên không được tạo chuỗi con")



