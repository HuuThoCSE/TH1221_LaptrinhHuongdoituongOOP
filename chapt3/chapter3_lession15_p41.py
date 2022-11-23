import string
c=input("Nhập chuỗi: ")
cm=c.split(" ")
cm.reverse()
for i in range (0,len(cm)):
    print(cm[i], end= " ")
