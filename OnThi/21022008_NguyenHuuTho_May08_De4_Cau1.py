#Nguyễn Hữu Thọ, 21022008, đề 04, máy 08
from datetime import date
import operator
class NGUOIHOC():
    def __init__(self, ms="", ht="", ns=date(2022, 12, 9), dt=0.0):
        self.ms = ms
        self.ht = ht
        self.ns = ns
        self.dt = dt

    def Nhap(self):
        self.ms = input("Nhập Mã số: ")
        ht = input("Nhập Họ tên: ")
        self.ht = ht.strip()
        ngay = int(input("Nhập Ngày sinh: "))
        while ngay <=0 or ngay > 31:
            ngay = int(input("Nhập lại ngày sinh: "))
        thang = int(input("Nhập Tháng sinh: "))
        while thang <=0 or thang > 12:
            thang = int(input("Nhập lại ngày sinh: "))
        nam = int(input("Nhập Năm sinh: ")) #THIẾU SÓT
        while(nam > date.today().year):
            nam = int(input("Nhập lại Năm sinh: "))
        self.ns = date(nam, thang, ngay)
        diemthi = float(input("Nhập điểm thi: ")) #THIẾU SÓT
        while(diemthi < 0 or diemthi > 10):
            diemthi = float(input("Nhập lại điểm thi: "))
        self.dt = diemthi

    def Xuat(self):
        print("Mã số:", self.ms)
        print("Họ tên:", self.ht)
        print("Ngày sinh:", self.ns.strftime("%d/%m/%Y"))
        print("Điểm thi:", self.dt)

    def Ten(self):
        khoangtrang = self.ht.rfind(" ")
        ten = self.ht[khoangtrang+1:len(self.ht)]
        return ten

    def __sub__(self, Number):
        diem = self.dt - Number
        if(diem <= 0): #THIẾU SÓT
            diem = 0
        elif(diem > 10):
            diem = 10
        self.dt = diem
        return diem

class NGUOIHOC_CB(NGUOIHOC):
    trinhdo = "CB"
    def __init__(self, ms="", ht="", ns=date(2022, 12, 9), dt=0.0, sdt=""):
        super(NGUOIHOC_CB, self).__init__(ms, ht, ns, dt)
        self.sdt = sdt

    def Nhap(self):
        NGUOIHOC.Nhap(self)
        self.sdt = input("Nhập Số điện thoại: ")

    def Xuat(self):
        NGUOIHOC.Xuat(self)
        print("Trình độ:", self.trinhdo)
        print("Số diện thoại:", self.sdt)

Nguoi1 = NGUOIHOC("21022008", "Nguyen Huu Tho", date(2003, 5, 26), 10)
Nguoi1.Xuat()
print()

Nguoi2 = NGUOIHOC()
Nguoi2.Nhap()
print()
Nguoi2.Xuat()
print()

diemtru = float(input("Nhập vào điểm trừ: "))
print("Điểm đã được trừ:", Nguoi2.__sub__(diemtru))
print()

Nguoi3 = NGUOIHOC_CB("21022018", "Nguyen Huu Phuoc", date(2003, 8, 1), 10, "0355865681")
Nguoi3.Xuat()
print()

DSNH = []
N = int(input("Nhập số lượng người học: "))
for i in range(1, N+1):
    print(f"===Nhập thông tin người học {i}:")
    Obj = NGUOIHOC_CB()
    Obj.Nhap()
    DSNH.append(Obj)
    print()

print("=====DANH SÁCH SINH VIÊN: ")
for i in range(0, len(DSNH)):
    print(f"===Thông tin người học {i+1}:")
    DSNH[i].Xuat()
    print()

# Số học sinh sinh vào quý 2
dem=0
for i in range(0, len(DSNH)):
    if(3 < DSNH[i].ns.month < 7):
        dem += 1
print(f"Có {dem} sinh viên sinh vào quý 2.")
print()

# Tên của người học có số điện thoại bắt đầu từ 0919
print("Tên của người học có số diện thoại bắt đầu từ 0919: ")
for i in range(0, len(DSNH)):
    if(str(DSNH[i].sdt[:4]) == "0919"):
        print(DSNH[i].Ten())
print()

# Sắp xếp DS người học tăng dần theo điểm thi và in danh sách sau khi sắp xếp
DSNH.sort(key=operator.attrgetter('dt'))
print("=====DANH SÁCH SINH VIÊN TĂNG DẦN (THEO ĐIỂM THI): ")
for i in range(0, len(DSNH)):
    print(f"===Thông tin người học {i+1}:")
    DSNH[i].Xuat()
    print()

#Nguyễn Hữu Thọ, 21022008, đề 04, máy 08