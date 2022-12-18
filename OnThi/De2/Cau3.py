from datetime import date
from dateutil.relativedelta import relativedelta

class MAYTINH():
    loai = 'PC'
    def __init__(self, soseri='', tenhang='', ngaymua=date(2022, 12, 16), giatien=0):
        self.soseri = soseri
        self.tenhang = tenhang
        self.ngaymua = ngaymua
        self.giatien = giatien

    def nhap(self):
        self.soseri = input("Nhập số seri: ")
        self.tenhang = input("Nhập tên hàng: ")
        ngay = int(input("Nhập ngày mua: "))
        thang = int(input("Nhập tháng mua: "))
        nam = int(input("Nhập năm mua: "))
        self.ngaymua = date(nam, thang, ngay)
        self.giatien = int(input("Nhập giá tiền: "))

    def NgayHetHangBaoHanh(self):
        return self.ngaymua+relativedelta(months=12)

    def xuat(self):
        print("Loại:", self.loai)
        print("Số seri:", self.soseri)
        print("Tên hãng:", self.tenhang)
        print("Ngày hết hạng bảo hành:", self.NgayHetHangBaoHanh().strftime("%d/%m/%Y"))
        print("Giá tiền:", self.giatien)

    def __mul__(self, number):
        return self.giatien*number

class LAPTOP(MAYTINH):
    def __init__(self, soseri='', tenhang='', ngaymua=date(2022, 12, 16), giatien=0, cannang=0):
        super(LAPTOP, self).__init__(soseri, tenhang, ngaymua, giatien)
        self.cannang = cannang

    def nhap(self):
        MAYTINH.nhap(self)
        self.cannang = float(input("Nhập cân nặng: "))

    def xuat(self):
        MAYTINH.xuat(self)
        print("Cân nặng:", self.cannang)


Item1 = MAYTINH()
# Item1.xuat()
print()

Item2 = MAYTINH("112233", "Laptop", date(2022, 12, 16), 200000)
Item2.xuat()

# songuyen = int("Nhập vào 1 số nguyên: ")
# print("Số tiền được nhân lên:", Item2.__mul__(songuyen))
print()

Item3 = LAPTOP()
# Item3.nhap()
Item3.xuat()
print()

# N = int(input("Nhập vào số lượng Laptop: "))
# DS_LAPTOP = []
N = 3
DS_LAPTOP = [
    LAPTOP("111", "DELL", date(2022, 12, 18), 300, 1.5),
    LAPTOP("112", "SAMSUNG", date(2022, 12, 18), 400, 1.4),
    LAPTOP("113", "Sony", date(2022, 12, 18), 500, 1.8)
]
# for i in range(0, N):
#     Obj = LAPTOP()
#     Obj.nhap()
#     DS_LAPTOP.append(Obj)

for i in range(0, N):
    DS_LAPTOP[i].xuat()
print()

#------------
max = DS_LAPTOP[0].cannang
for i in range(1, N):
    if DS_LAPTOP[i].cannang > max:
        max = DS_LAPTOP[i].cannang

print("Số seri laptop nặng nhất:", end="")
for i in range(0, N):
    if DS_LAPTOP[i].cannang == max:
        print(DS_LAPTOP[i].soseri)

#----- Xap xem LAPTOP tang dang
import operator
print("Sắp xếp theo thứ tự tăng dần của kg")
DS_LAPTOP.sort(key=operator.attrgetter('cannang'))
for i in range(0, N):
    print(DS_LAPTOP[i].xuat())
    print()

print("Sắp xếp theo thứ tự giảm dần của kg")
DS_LAPTOP.sort(key=operator.attrgetter('cannang'), reverse=True)
for i in range(0, N):
    print(DS_LAPTOP[i].xuat())
    print()

#11:18

