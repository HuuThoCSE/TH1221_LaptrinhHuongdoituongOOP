import math
class ToaDo:
    def __init__(self, HoanhDo=0, TungDo=0):
        self.x = HoanhDo
        self.y = TungDo
    def Nhap(self):
        self.x = int(input("Nhập hoành độ: "))
        self.y = int(input("Nhập tung độ: "))
    def Xuat(self):
        print("{", format(self.x, '.4f'), ",", format(self.y, '.4f'),"}")
    def KhoangCach(self, ToaDo2): # Tính khoảng cách giữa 2 tọa độ
        khoangcach = math.sqrt((ToaDo2.x-self.x)**2+(ToaDo2.y-self.y))
        return khoangcach
    def __sub__(self, ToaDo2):
        x = self.x - ToaDo2.x
        y = self.y - ToaDo2.y
        return ToaDo(x, y)
    def __mul__(self, ToaDo2):
        x = self.x*ToaDo2.x
        y = self.y*ToaDo2.y
        return ToaDo(x, y)
    def __floordiv__(self, ToaDo2): #Chia lấy phần nguyên
        x = self.x // ToaDo2.x
        y = self.y // ToaDo2.y
        return ToaDo(x, y)
    def __and__(self, ToaDo2):
        if(self.x > 0 and ToaDo2.x > 0 and ToaDo2.x > 0 and ToaDo2.y > 0):
            return True
        else:
            return False

A = ToaDo(2,3)
# A.Nhap()
A.Xuat()

B = ToaDo(4,5)
B.Xuat()

print("Khoang cach giua A va B la: ", A.KhoangCach(B))

C = A-B
C.Xuat()

D = A*B
D.Xuat()

# E = A.__floordiv__(B) - Ok
E = A//B
E.Xuat()

if(A and B):
    print("Điểm A và B thuộc góc phần từ thứ nhất.")
else:
    print("Điểm A và B không thuộc góc phần từ thứ nhất.")
