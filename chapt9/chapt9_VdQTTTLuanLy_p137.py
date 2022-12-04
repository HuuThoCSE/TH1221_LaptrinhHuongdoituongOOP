from datetime import date
class Connguoi:
    '''Lớp con người gồm 7 thuộc tính, 6 phương thức và 3 hàm quá tải'''
    dangdi = 'thẳng'
    trikhon = 'có'

    def __init__(self, md='vàng', mm='den', nm='AB', qt='Việt Nam', ns=date(1975, 6, 22)):
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
        print('Dáng đi: ', self.dangdi)
        print('Trí khôn: ', self.trikhon)
        print('Màu da: ', self.mauda)
        print('Màu mắt', self.maumat)
        print('Nhóm máu; ', self.nhommau)
        print('Quốc tịch: ', self.quoctich)
        print('Ngày sinh', self.ngaysinh.strftime("%d/%m/%Y"))

    def Nhommau(self):
        return self.nhommau

    def Quoctich(self):
        return self.quoctich

    def Namsinh(self):
        return self.ngaysinh.year

    def __and__(self, ob2):
        if(self.Quoctich() == ob2.Quoctich()):
            return True
        else:
            return False

    def __or__(self, ob2):
        if(self.Nhommau()=='AB' or ob2.Nhommau()=='AB'):
            return True
        else:
            return False

    def __invert__(self):
        if(date.today().year-self.Namsinh()!=19):
            return True
        else:
            return False

P1 = Connguoi()
P1.Nhap()
print('Thông tin về P1: ')
P1.Xuat()

P2 = Connguoi()
P2.Nhap()
print('Thông tin về P2: ')
P2.Xuat()

if(P1.__and__(P2) == True):
    print('Hai người cùng quốc tịch')
else:
    print('Hai người KHÔNG cùng quốc tịch')

if(P1.__or__(P2)==True):
    print('Có ít nhất 1 người có nhóm máu AB')
else:
    print('Cả 2 người đều KHÔNG có nhóm máu AB')

if(P1.__invert__()==True):
    print('Người ngày KHÔNG PHẢI 19 tuổi')
else:
    print('Người này 19 tuổi')