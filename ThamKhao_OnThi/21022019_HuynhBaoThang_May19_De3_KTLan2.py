# Huỳnh Bảo Thắng , 21022019,Đề 3,Máy 19
from datetime import date
class HOCVIEN:
    def __init__(self):
        self.mshv = '21022019'
        self.ht = 'Huỳnh Bảo Thắng'
        self.ngaysinh = date(2003,1,19)
        self.dt = 9
    def Nhap(self):
        self.mshv = input("Nhập mã số học viên:")
        self.ht = input("Nhập họ tên:")
        ngay = int(input("Nhập ngày sinh:"))
        thang = int(input("Nhập tháng sinh:"))
        nam = int(input("Nhập năm sinh:"))
        self.ngaysinh = date(nam,thang,ngay)
        self.dt = float(input("Nhập diểm thi:"))
    def Xuat(self):
        print("Mã số học viên:",self.mshv)
        print("Họ tên:",self.ht)
        print("Ngày sinh:",self.ngaysinh.strftime("%d/%m/%Y"))
        print("Điểm thi:",self.dt)
    def Chuoicon(self):
        ktc = self.ht.rfind(" ")
        ten = self.ht[ktc+1:]
        return ten
    def __add__(self, x):
        self.dt = self.dt + x

HV = HOCVIEN()
print("Nhập thông tin Học viên:")
HV.Nhap()
print()
print("Thông tin của Học viên này là:")
HV.Xuat()
print()
print("Tên của học viên này là:",HV.Chuoicon())
print()
x = float(input("Nhập số thực bất kì:"))
HV.__add__(x)
print()
print("Thông tin của Học viên sau khi cộng thêm vào điểm thi là:")
HV.Xuat()
print()
class HOCVIEN_NC(HOCVIEN):
    trinhdo = 'NC'
    def __init__(self):
        super().__init__()
        self.sdt = '0123456789'
    def Nhap1(self):
        self.Nhap()
        self.sdt =input("Nhập số điện thoại:")
    def Xuat1(self):
        print("Trình độ:",self.trinhdo)
        self.Xuat()
        print("Số điện thoại:",self.sdt)
HVNC = HOCVIEN_NC()
print("Nhập thông tin của Học viên:")
HVNC.Nhap1()
print()
print("Thông tin của Học viên là:")
HVNC.Xuat1()
print()
N = int(input("Nhập số lượng học viên:"))
while N<=0:
    N = int(input("Nhập số lượng học viên:"))
ds=[]
for i in range(N):
    H = HOCVIEN_NC()
    H.Nhap1()
    ds.append(H)
    print()
print("Danh sách học viên lớp HOCVIEN_NC:")
for i in ds:
    i.Xuat1()
    print()
dem = 0
for i in ds:
    if i.ngaysinh.day == 5 or i.ngaysinh.day == 15 or i.ngaysinh.day == 25:
        dem +=1
print("Có",dem,"học viên sinh vào các ngày 5,15,25")
print()
print("Tên của các học viên có số điện thoại bắt đầu là '0907':")
for i in ds:
    kt = i.sdt.find('0907',0,4)
    if kt==0:
        print(i.ht)
print()
for i in range(N-1):
    for j in range(i+1,N):
        if ds[i].dt < ds[j].dt:
            ds[i],ds[j] = ds[j],ds[i]
print("Danh sách sau khi sắp xếp theo điểm thi giảm dần là:")
for i in ds:
    i.Xuat1()
    print()
# Huỳnh Bảo Thắng , 21022019,Đề 3,Máy 19