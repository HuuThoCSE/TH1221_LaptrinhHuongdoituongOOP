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
    def __init__(self, MauSac=""):
        super().__init__(self)

        self.MauSac = MauSac

    def ValueMauSac(self):
        return self.MauSac

class HinhTron(ToaDoMau):
    def __init__(self):
        super().__init__(self)


A = ToaDo(2, 3)
A.Xuat()