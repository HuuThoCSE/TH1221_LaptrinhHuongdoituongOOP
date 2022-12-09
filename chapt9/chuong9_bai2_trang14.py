from datetime import date, timedelta
class ConNguoi:
    dangdi = "Thẳng"
    trikhon = "Có"
    def __init__(self, mauda="", maumat="", nhommau="", quoctich="", ngaysinh=date(2022, 12, 8)):
        self.mauda = mauda
        self.maumat = maumat
        self.nhommau = nhommau
        self.quoctich = quoctich
        self.ngaysinh = ngaysinh

    def Nhap(self):
        self.mauda = input("Nhập màu da: ")
        self.maumat = input("Nhập màu mắt: ")
        self.nhommau = input("Nhập nhóm máu: ")
        self.quoctich = input("Nhập quốc tịch: ")
        ngay = int(input("Nhập ngày sinh: "))
        thang = int(input("Nhập tháng sinh: "))
        nam = int(input("Nhập năm sinh: "))
        self.ngaysinh = date(nam, thang, ngay)
    def Xuat(self):
        print("Dáng đi:", self.dangdi)
        print("Trí khôn:", self.trikhon)
        print("Màu da:", self.mauda)
        print("Nhóm máu:", self.nhommau)
        print("Quốc tịch:", self.quoctich)
        print("Ngày sinh:", self.ngaysinh.strftime("%d/%m/%Y"))

    def MauDa(self):
        return self.mauda

    def MauMat(self):
        return self.maumat

    def NgaySinh(self):
        return self.ngaysinh.strftime("%d/%m/%Y")

    def __add__(self, Number):
        self.ngaysinh = self.ngaysinh+timedelta(days=Number)
        return self.ngaysinh.strftime("%d/%m/%Y")

    def __sub__(self, Number):
        self.ngaysinh = self.ngaysinh-timedelta(days=Number)
        return self.ngaysinh.strftime("%d/%m/%Y")

    def __and__(self, Nguoi2):
        if(self.ngaysinh == Nguoi2.ngaysinh):
            return True
        else:
            return False
    def __or__(self, Nguoi2):
        if(self.maumat=="Xanh" or Nguoi2.maumat=="Xanh"):
            return True
        else:
            return False

    def __xor__(self, Nguoi2):
        if(self.mauda=="Trắng" or self.mauda=="Vàng" and Nguoi2.mauda=="Trắng" or Nguoi2.mauda=="Vàng"):
            return True
        else:
            return False

    def __not__(self, Nguoi2):
        if(self.ngaysinh != Nguoi2.ngaysinh):
            return True
        else:
            return False

    def __gt__(self, Nguoi2):
        if(self.ngaysinh > Nguoi2.ngaysinh):
            return True
        else:
            return False

    def __ge__(self, Nguoi2):
        if (self.ngaysinh > Nguoi2.ngaysinh):
            return True
        else:
            return False

    def __lt__(self, Nguoi2):
        if(self.ngaysinh < Nguoi2.ngaysinh):
            return True
        else:
            return False

    def __le__(self, Nguoi2):
        if(self.ngaysinh <= Nguoi2.ngaysinh):
            return True
        else:
            return False

    def __eq__(self, Nguoi2):
        if(self.ngaysinh == Nguoi2.ngaysinh):
            return True
        else:
            return False

    def __ne__(self, Nguoi2):
        if(self.ngaysinh == Nguoi2.ngaysinh):
            return True
        else:
            return False

ConNguoi1 = ConNguoi()
ConNguoi1.Xuat()
print(ConNguoi1.MauDa())
print(ConNguoi1.MauMat())
print(ConNguoi1.NgaySinh())
print("===")

ConNguoi2 = ConNguoi("Vàng", "Đen", "AB", "Việt Nam", date(2003, 5, 25))
ConNguoi2.Xuat()
print("====")

# n = int(input("Nhập vào n (+ngaysinh): "))
# print(ConNguoi2.__add__(n))
# print(ConNguoi2-n)

ConNguoi3 = ConNguoi("Trắng", "Đen", "AB", "Việt Nam", date(2003, 5, 27))
ConNguoi3.Xuat()
print()

ConNguoi4 = ConNguoi("Vàng", "Xanh", "AB", "Việt Nam", date(2003, 5, 26))

if(ConNguoi2.__and__(ConNguoi3)): #Phải dùng __and__
    print("2 người có cùng ngày sinh.")
else:
    print("2 người không cùng ngày sinh.")

if(ConNguoi3.__or__(ConNguoi4)):
    print("Có một người có mắt màu xanh.")
else:
    print("Không có người nào có mắt màu xanh.")

if(ConNguoi3.__xor__(ConNguoi4)):
    print("Có 1 người có da màu trắng và có một người có da màu vàng.")
else:
    print("Không có người có da màu trắng và không có người có da màu vàng.")

if(ConNguoi3.__not__(ConNguoi4)):
    print("Không trùng ngày sinh.")
else:
    print("Trùng ngày sinh.")

# Quá tải toán tử so sánh
if(ConNguoi2.__gt__(ConNguoi3)):
    print("Tuổi người 1 lớn hơn tuổi người 2.")
else:
    print("Tuổi người 1 không lớn hơn tuổi người 2.")

if(ConNguoi2.__ge__(ConNguoi3)):
    print("Tuổi người 1 lớn hơn bằng tuổi người 2.")
else:
    print("Tuổi người 1 không lớn hơn bằng tuổi người 2.")

if(ConNguoi2 < ConNguoi3):
    print("Tuổi người 1 nhỏ hơn tuổi người 2.")
else:
    print("Tuổi người 1 nhỏ lớn hơn tuổi người 2.")

if(ConNguoi2 <= ConNguoi3):
    print("Tuổi người 1 nhỏ hơn bằng tuổi người 2.")
else:
    print("Tuổi người 1 không nhỏ hơn bằng tuổi người 2.")

if(ConNguoi2 == ConNguoi3):
    print(ConNguoi2.NgaySinh())
else:
    print(ConNguoi3.NgaySinh())

if(ConNguoi2 != ConNguoi3):
    print(ConNguoi2.NgaySinh())
else:
    print(ConNguoi3.NgaySinh())