from datetime import date
class Connguoi:
    '''Nội dung lớp con người'''
    dangdi = 'thẳng'
    trikhon = 'có'
    def __init__( self, md='vàng', mm='đen', nm='AB', qt='Việt Nam', ns=date(1975,6,22) ):
         self.mauda = md
         self.maumat = mm
         self.nhommau = nm
         self.quoctich = qt
         self.ngaysinh = ns
    def Nhap(self):
         self.mauda = input("Nhập màu da:")
         self.maumat = input("Nhập màu mắt:")
         self.nhommau = input("Nhập nhóm máu:")
         self.quoctich = input("Nhập quốc tịch:")
         ngay = int(input("Nhập ngày sinh:") )
         thang = int(input("Nhập tháng sinh:") )
         nam = int(input("Nhập năm sinh:") )
         self.ngaysinh = date(nam, thang, ngay)
    def Xuat(self):
     print('Dáng đi:', self.dangdi)
     print('Trí khôn:', self.trikhon)
     print('Màu da:', self.mauda)
     print('Màu mắt:', self.maumat)
     print('Nhóm máu:', self.nhommau)
     print('Quốc tịch:', self.quoctich)
     print( 'Ngày sinh:', self.ngaysinh.strftime("%d/%m/%Y") )

    def Nhommau(self):
         return self.nhommau

    def Quoctich(self):
         return self.quoctich

    def Namsinh(self):
         return self.ngaysinh.year

    def Sosanh(self, Person):
         if self.ngaysinh.year < Person.ngaysinh.year:
             return 1
         elif self.ngaysinh.year > Person.ngaysinh.year:
             return -1
         elif self.ngaysinh.month < Person.ngaysinh.month:
             return 1
         elif self.ngaysinh.month > Person.ngaysinh.month:
             return -1
         elif self.ngaysinh.day < Person.ngaysinh.day:
            return 1
         elif self.ngaysinh.day > Person.ngaysinh.day:
            return -1
         else:
             return 0

Person1 = Connguoi()
print('Thông tin về Person1:')
Person1.Xuat()
Person2 = Connguoi()
print('Nhập thông tin cho Person2:')
Person2.Nhap()
print('Thông tin về Person2:')
Person2.Xuat()
print('Nhóm máu của Person1 là:', Person1.Nhommau())
print('Quốc tịch của Person2 là:', Person2.Quoctich())
print('Tuổi của Person1 là:', date.today().year - Person1.Namsinh())

if Person1.Sosanh(Person2) == 1:
    print('Person1 lớn hơn Person2')
elif Person1.Sosanh(Person2) == -1:
    print('Person1 nhỏ hơn Person2')
else:
    print('Person1 bằng Person2')