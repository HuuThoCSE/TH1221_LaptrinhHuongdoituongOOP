#H/PH/S
h = int(input("Nhap vao gio: "))
ph = int(input("Nhap vao phut: "))
while ph >= 60:
    print("vui long nhap lai")
    ph = int(input("Nhap vao phut: "))
s = int(input("Nhap vao giay: "))
while s >= 60:
    print("vui long nhap lai")
    s = int(input("Nhap vao giay: "))
print("Thời gian: ",h,"giờ :",ph,"phút :",s,"giây")
P=int(input("Nhap vao phut cong them: "))
x=P+ph
if x>=60:
    t = x//60
    h = h + t
    ph = x%60
print("Thời gian: ",h,"giờ :",ph,"phút :",s,"giây")



