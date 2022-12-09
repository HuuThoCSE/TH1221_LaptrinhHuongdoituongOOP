from datetime import date
import operator
class Connguoi:
    dangdi = 'thẳng'
    trikhon = 'có'

    def __init__( self, md='vàng', mm='đen', nm='AB', qt='Việt Nam', ns=date(1975,6,22) ):
        self.mauda = md
        self.maumat = mm
        self.nhommau = nm
        self.quoctich = qt
        self.ngaysinh = ns

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
        print('Dáng đi:', self.dangdi)
        print('Trí khôn:', self.trikhon)
        print('Màu da:', self.mauda)
        print('Màu mắt:', self.maumat)
        print('Nhóm máu:', self.nhommau)
        print('Quốc tịch:', self.quoctich)
        print( 'Ngày sinh:', self.ngaysinh.strftime("%d/%m/%Y") )

    def mauda (self):
        return self.mauda

    def maumat (self):
        return self.maumat

    def ngsinh (self):
        return self.ngaysinh.strftime("%d/%m/%Y")

    def __add__ (self, n):
        d = self.ngaysinh.day + n
        m = self.ngaysinh.month + n
        y = self.ngaysinh.year +  n
        self.ngaysinh = date(y, m, d)
        return self.ngaysinh.strftime("%d/%m/%Y")

    def __sub__ (self, n):
        d = self.ngaysinh.day - n
        m = self.ngaysinh.month - n
        y = self.ngaysinh.year -  n
        self.ngaysinh = date(y, m, d)
        return self.ngaysinh.strftime("%d/%m/%Y")

    def __and__ (self, other):
        if self.ngaysinh.day == other.ngaysinh.day \
                and self.ngaysinh.month == other.ngaysinh.month:
            return True
        else:
            return False

    def __or__ (self, other):
        if self.maumat == 'Màu xanh' or other.maumat == 'Màu xanh':
            return True
        else:
            return False

    def __xor__(self, other):
        if operator.xor (self.mauda == 'Màu trắng', other.mauda == 'Màu vàng'):
            return True
        else:
            return False

    def __not__ (self):
        if self.ngaysinh.day != 5:
            return True
        else:
            return False

    def __gt__(self, other):
        if date.today().year - self.ngaysinh.year > date.today().year - other.ngaysinh.year:
            return True
        else:
            return False

    def __ge__(self, other):
        if date.today().year - self.ngaysinh.year >= date.today().year - other.ngaysinh.year:
            return True
        else:
            return False

    def __lt__(self, other):
        if date.today().year - self.ngaysinh.year < date.today().year - other.ngaysinh.year:
            return True
        else:
            return False

    def __le__(self, other):
        if date.today().year - self.ngaysinh.year <= date.today().year - other.ngaysinh.year:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.ngaysinh.day == other.ngaysinh.day \
                and self.ngaysinh.month == other.ngaysinh.month \
                and self.ngaysinh.year == other.ngaysinh.year:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.ngaysinh.day != other.ngaysinh.day \
                and self.ngaysinh.month != other.ngaysinh.month \
                and self.ngaysinh.year != other.ngaysinh.year:
            return True
        else:
            return False

P1 = Connguoi()
P1.Nhap()
print('Thông tin về P1:')
P1.Xuat()

P2 = Connguoi()
P2.Nhap()
print('Thông tin về P2:')
P2.Xuat()

# QTTT số học
k = int(input('Nhập số cần cộng:'))
print('Cộng ngày sinh:', P1.__add__(n=k))
print('Trừ ngày sinh:', P1.__sub__(n=k))

# QTTT luận lý
if P1.__and__(P2) == True:
    print('Hai người có cùng ngày sinh nhật.')
else:
    print('Hai người không cùng ngày sinh nhật.')

if P1.__or__(P2) == True:
    print('Một trong 2 người có màu mắt xanh.')
else:
    print('Hai người không có ai màu mắt xanh.')

if P1.__xor__(P2) == True:
    print ('Có 1 người da trắng và 1 người da vàng.')
else:
    print('1 trong 2 người không có 1 người da trắng và 1 người da vàng.')

if P1.__not__() == True:
    print('Người này không có cùng ngày sinh.')
else:
    print ('Người này trùng ngày sinh.')

# QTTT SS
if P1.__gt__(P2) == True:
    print('Tuổi người 1 lớn hơn tuổi người 2.')
else:
    print('Tuổi người 1 không lớn hơn tuổi người 2.')

if P1.__ge__(P2) == True:
    print ('Tuổi người 1 lớn hơn hoặc bằng tuổi người 2.')
else:
    print('Tuổi người 1 nhỏ hơn tuổi người 2.')

if P1.__lt__(P2) == True:
    print ('Tuổi người 1 nhỏ hơn tuổi người 2.')
else:
    print('Tuổi người 1 không nhỏ hơn tuổi người 2.')

if P1.__le__(P2) == True:
    print ('Tuổi người 1 nhỏ hơn hoặc bằng tuổi người 2.')
else:
    print('Tuổi người 1 lớn hơn tuổi người 2.')

if P1.__eq__(P2) == True:
    print ('Tuổi người 1 bằng tuổi người 2.')
else:
    print('Tuổi người 1 không bằng tuổi người 2.')

if P1.__ne__(P2) == True:
    print ('Tuổi người 1 không bằng tuổi người 2.')
else:
    print('Tuổi người 1 bằng tuổi người 2.')