class Fraction():
    def __init__(self, tuso=0, mauso=0):
        self.tuso = tuso
        self.mauso = mauso

    def Nhap(self):
        self.tuso = int(input("Nhập tử số: "))
        mauso = int(input("Nhập mẫu số: "))
        while(mauso == 0):
            mauso = int(input("Nhập lại mẫu số: "))
        self.mauso = mauso

    def Xuat(self):
        if(self.tuso == 0):
            print(0)
        elif(self.mauso == 1):
            print(self.tuso)
        elif self.tuso < 0 and self.mauso < 0:
            print(abs(self.tuso),"/",abs(self.mauso))
        elif self.tuso > 0 and self.mauso < 0:
            print(-self.tuso, "/", abs(self.mauso))
        else:
            print(self.tuso, "/", self.mauso)

    def ToiGian(self):
        if self.tuso < self.mauso:
            i = self.tuso
        else:
            i = self.mauso
        while self.tuso % i != 0 or self.mauso % i != 0:
            i-=1
        tu = self.tuso // i
        mau = self.mauso // i
        return Fraction(tu, mau)

    def __add__(self, PhanSo2):
        ts = self.tuso + PhanSo2.tuso
        ms = self.mauso + PhanSo2.mauso
        return Fraction(ts, ms)

    def __sub__(self, PhanSo2):
        ts = self.tuso - PhanSo2.tuso
        ms = self.mauso - PhanSo2.mauso
        return Fraction(ts, ms)

    def __mul__(self, PhanSo2):
        ts = self.tuso * PhanSo2.tuso
        ms = self.mauso * PhanSo2.mauso
        return Fraction(ts, ms)

    def __pow__(self, Number):
        ts = self.tuso ** Number
        ms = self.mauso ** Number
        return Fraction(ts, ms)

    def __truediv__(self, PhanSo2):
        ts = self.tuso / PhanSo2.tuso
        ms = self.mauso / PhanSo2.mauso
        return Fraction(ts, ms)

    def __floordiv__(self, PhanSo2):
        ts = self.tuso // PhanSo2.tuso
        ms = self.mauso // PhanSo2.mauso
        return Fraction(ts, ms)

    def __mod__(self, PhanSo2):
        ts = self.tuso % PhanSo2.tuso
        ms = self.mauso % PhanSo2.mauso
        return Fraction(ts, ms)

    def __and__(self, PhanSo2):
        if(self.tuso > 0 and PhanSo2.tuso > 0 and self.mauso > 0 and PhanSo2.mauso > 0):
            return True
        else:
            return False

    def __or__(self, PhanSo2):
        if(self.tuso > 0 and self.mauso > 0 or PhanSo2.tuso >0 and PhanSo2.mauso > 0):
            return True
        else:
            return False

    def __xor__(self, PhanSo2):
        if(self.tuso < 0 and self.mauso < 0 and PhanSo2.tuso > 0 and PhanSo2.mauso > 0):
            return True
        elif self.tuso > 0 and self.mauso > 0 and PhanSo2.tuso < 0 and PhanSo2.mauso < 0:
            return True
        else:
            return False

A1 = Fraction(1, 2)
A1.Xuat()

A2 = Fraction(2,-3)
A2.Xuat()

A3 = Fraction(6, 8)
A3.Xuat()
A4 = A3.ToiGian()
A4.Xuat()

A5 = A3.__add__(A4)
A5.Xuat()

A6 = A3.__sub__(A4)
A6.Xuat()

A7 = A3.__mul__(A4)
A7.Xuat()

A8 = A3.__pow__(2)
A8.Xuat()

A9 = A3.__truediv__(A4)
A9.Xuat()

A10 = A3.__floordiv__(A4)
A10.Xuat()

A11 = A3.__mod__(A4)
A11.Xuat()

if(A3.__and__(A4)):
    print("Cả 2 phân số đều dương.")
else:
    print("Cà 2 phân số có 1 số không dương.")

if(A3.__or__(A4)):
    print("Có ít nhất một phân số dương.")
else:
    print("Không có phân số nào là phân số dương.")

if(A3.__xor__(A4)):
    print("2 phân số, chỉ có 1 phân số dương.")
else:
    print("2 phân số, chỉ có 1 phân số dương.")