class Toado:
    '''Lớp tọa độ gồm 2 thuộc tính, 4 phương thức'''
    def __init__(self, hd=0, td=0):
        self.x = hd
        self.y = td

    def Nhap(self):
        self.x = float(input("Nhập hoành độ: "))
        self.y = float(input("Nhập tung độ: "))

    def Xuat(self):
        print('(', format(self.x, '.2f'), ', ', format(self.y, '.2f'), ')')

    def __add__(self, ob2):
        x = self.x + ob2.x
        y = self.y + ob2.y
        return Toado(x, y)

    def __pow__(self, n):
        x = pow(self.x, n)
        y = pow(self.y, n)
        return Toado(x, y)

    def __truediv__(self, ob2):
        x = self.x / ob2.x
        y = self.y / ob2.y
        return Toado(x, y)

    def __mod__(self, m):
        x = self.x % m
        y = self.y % m
        return Toado(x, y)

A = Toado()
print('Nhập tọa độ cho A: ')
A.Nhap()
print('Điểm A có tọa độ là: ')
A.Xuat()

B = Toado()
print('Nhập tọa độ cho B: ')
B.Nhap()
print('Điểm B có tọa độ là: ')
B.Xuat()

C = A.__add__(B)
# C = A + B

print('Điểm C = A + B có tọa độ là: ')
C.Xuat()

n = int(input("Nhập giá trị n= "))
D = A.__pow__(n)
# D = A ** n
print('Điểm D = A ** n có tọa độ là: ')
D.Xuat()

E = A.__truediv__(B)
# E = A / B
print('Điểm E = A / B có tọa độ là: ')
E.Xuat()
m = int(input('Nhập giá trị m= '))
F = B.__mod__(m)
# F = B % m
print('Điểm F = B % m có tọa độ là: ')
F.Xuat()
