import math
class Toado:
    '''Lớp tọa độ gồm 2 thuộc tính và 6 phương thức'''
    def __init__(self, hd = 0, td = 0):
        self.x = hd
        self.y = td
    def Nhap(self):
        self.x = float(input("Nhập hoành độ: "))
        self.y = float(input("Nhập tung độ: "))
    def Xuat(self):
        print('(',self.x,',',self.y,')')
    def Hoanhdo(self):
        return self.x
    def Tungdo(self):
        return self.y
    def Khoangcach(self, ob):
        kc = math.sqrt(pow(ob.x-self.x,2)+pow(ob.y-self.y,2))
        return kc

A = Toado(2, 3)
print('Điểm A có tọa độ là:')
A.Xuat()
B = Toado()
print('Điểm B có tọa độ là:')
B.Xuat()
print('Nhập tọa độ cho A:')
A.Nhap()
print('Điểm A có tọa độ là:')
A.Xuat()
print('Nhập tọa độ cho B:')
B.Nhap()
print('Điểm B có tọa độ là:')
B.Xuat()
C = Toado()
print('Nhập tọa độ cho C:')
C.Nhap()
print("Hoành độ của C là:",C.Hoanhdo())
print("Tung độ của C là:",C.Tungdo())
kcAB = A.Khoangcach(B)
print('Khoảng cách từ A đến B là:',kcAB)
kcAC = A.Khoangcach(C)
print('Khoảng cách từ A đến C là:',kcAC)
kcBC = B.Khoangcach(C)
print('Khoảng cách từ B đến C là:',kcBC)
if(kcAB+kcAC > kcBC and kcAB+kcBC > kcAC and kcAC+kcBC > kcAB):
    print('3 điểm A, B,C tạo thành một tam giác')
else:
    print('3 điểm A, B,C không tạo thành tam giác')