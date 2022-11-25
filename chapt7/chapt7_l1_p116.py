class Fraction:
    def __init__(self, TuSo, MauSo):
        self.TuSo = TuSo
        self.MauSo = MauSo

    def Nhap(self):
        self.TuSo = int(input("Nhập tử số: "))
        self.MauSo = int(input("Nhập mẫu số: "))
        while self.MauSo ==0:
            print("Giá trị mẫu số không hợp lệ,", end="")
            self.MauSo = int(input("nhập mẫu số: "))

    def InPhanSo(self):
        if self.TuSo == 0:
            print(0)
        elif self.MauSo ==1:
            print(self.TuSo)
        else:
            print("Phân số: ", self.TuSo ,"/", self.MauSo)

    def TuSo(self):
        return self.TuSo

    def MauSo(self):
        return self.MauSo

    def PhanSoNghichDao(self):
        return print(self.MauSo, "/", self.TuSo)

    def GiaTriThuc(self):
        return self.TuSo/self.MauSo

    def ToiGianPhanSo(self):
        pass

    def SoSanhHaiPhanSo(self):
        pass

    def CongHaiPhanSo(self):
        pass

    def TriHaiPhanSo(self):
        pass

    def NhanHaiPhanSo(self):
        pass

    def ChiaHaiPhanSo(self):
        pass

A = Fraction(2, 3)
A.InPhanSo()

B = Fraction(0, 3)
B.InPhanSo()

B = Fraction(3, 1)
B.InPhanSo()

C = Fraction(1, 2)
C.GiaTriThuc()
C.ToiGianPhanSo()
