import string
i=0
c=input("Nhập 1 chuỗi bất kì: ")
while i<len(c):
    if not c[i].isdigit() :
        c=c[:i]+c[i+1:]
    else:
        i+=1
print("Chuỗi sau khi xóa: ", c  )