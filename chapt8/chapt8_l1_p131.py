import math
class ToaDo:
    '''Lớp tọa độ gồm 2 thuộc tính và 6 phương thức'''
    def __init__(self, hd=0, td=0):
        self.x = hd
        self.y = td
    def Nhap(self):
        self.x = float(input("Nhập hoành độ: "))
        self.y = float(input("Nhập tung độ: "))

    def Xuat(self):
        print('(', self.x, ',', self.y, ')')

    def Hoanhdo(self):
        return self.x

    def Tungdo(self):
        return self.y

    def Khoangcach(self, ob):
        kc = math.sqrt(pow(ob.x - self.x, 2) + pow(ob.y - self.y, 2))
        return kc

class ToaDoMau(ToaDo):
    def __init__(self, hd, td, MauSac=""):
        super().__init__(hd, td)

        self.MauSac = MauSac

    def ValueMauSac(self):
        return self.MauSac

    def Nhap(self):
        ToaDo.Nhap(self)
        self.MauSac = input("Màu: ")

    def Xuat(self):
        ToaDo.Xuat(self)
        print("Màu:", self.MauSac)

class HinhTron(ToaDoMau):
    def __init__(self, hd=0, td=0, MauSac="",BanKinh=0):
        super().__init__(hd, td, MauSac)
        self.r = BanKinh

    def Nhap(self):
        ToaDoMau.Nhap(self)
        self.r = int(input("Nhập bán kính: "))

    def Xuat(self):
        ToaDoMau.Xuat(self)
        print("Bán kính:", self.r)

    def KiemTra1DiemCoThuocDuongTron(self, Diem):
        d = math.sqrt(abs(Diem.x - self.x)**2 + abs(Diem.y - self.y)**2)
        if(self.r==d):
            return True
        else:
            return False


A = ToaDo(2, 3)
A.Xuat()

B = ToaDoMau(4, 6, "Red")
# B.Nhap()
B.Xuat()
print()

C = HinhTron(6, 9, "Vàng",3)
# C.Nhap()
C.Xuat()

HinhTron = HinhTron()
HinhTron.Nhap()

PointInHTr = ToaDo()
PointInHTr.Nhap()

if(HinhTron.KiemTra1DiemCoThuocDuongTron(PointInHTr)):
    print(f"Điểm ({PointInHTr.x}, {PointInHTr.y}) thuộc hình tròn")
else:
    print(f"Điểm ({PointInHTr.x}, {PointInHTr.y}) không thuộc hình tròn")