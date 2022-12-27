class SACH:
    def __int__(self,mas=0,nn=0,dongia=0,sl=0,nxb=0):
        self.mas = mas
        self.nn = nn
        self.dongia = dongia
        self.sl = sl
        self.nxb = nxb
    def Nhap(self):
        self.mas = input('Nhap ma sach: ')
        self.nn = input('Nhap ngay nhap: ')
        self.dongia = int(input('Nhap don gia: '))
        self.sl = int(input('Nhap so luong: '))
        self.nxb = input('NHap nha xuat ban: ')
    def Xuat(self):
        print('Ma sach la: ',self.mas)
        print('Ngay nhap la: ',self.nn)
        print('Don gia la: ',self.dongia)
        print('So luong la: ',self.sl)
        print('Nha xuat ban la: ',self.nxb)
class STK(SACH):
    def __int__(self,mas=0,nn=0,dongia=0,sl=0,nxb=0,thue=0):
        SACH.__init__(self)
        self.thue = thue
    def NhapSTK(self):
        SACH.Nhap(self)
        self.thue = int(input('Nhap thue: '))
    def XuatSTK(self):
        SACH.Xuat(self)
        print('Thue la: ',self.thue)
    def TienSTK(self):
        self.tt = self.sl * self.dongia + self.thue
class SGK(SACH):
    def __int__(self,mas=0,nn=0,dongia=0,sl=0,nxb=0,tt=0):
        SACH.__init__(self)
        self.tt = tt
    def NhapSGK(self):
        SACH.Nhap(self)
        self.tt = int(input('Tinh trang moi nhap 1, cu nhap 0: '))
    def XuatSGK(self):
        SACH.Xuat(self)
        if self.tt == 1:
            print('Tinh trang: moi ')
        elif self.tt == 0:
            print('Tinh trang: cu ')
    def TienSGK(self):
        if self.tt == 1:
            self.ttmoi = self.sl * self.dongia
        elif self.tt == 0:
            self.ttcu = self.sl * self.dongia * 50/100


#Nhap n doi tuong luon SGK
ds = []
n=int(input('Nhap n doi tuong sach: '))
while n<0 or n>30:
    print('Vui long nhap lai')
for i in range(1, n+1):
    print('Thong tin sach thu ',i)
    A = SGK()
    A.NhapSGK()
    ds.append(A)

#in n doi tuong sach
for i in ds:
    i.XuatSGK()
    print('\n')
#tinh tong thanh tien cho cac loai sach giao khoa  dc xuat ban tai NXB dhCt
x = input('==Nhap vao ten nha xuat ban: ')
d = 0
dem = 0
tong = 0
for i in ds:
    if i.nxb == x and i.tt == 1:
        d += 1
        i.TienSGK()
    elif i.nxb == x and i.tt == 0:
        dem += 1
        i.TienSGK()
print('==Tong tien sach duoc xuat ban tai NXB DHCT: ',)
#thong ti sach gia khoa co don gia nho nhat
import math
min = 0
for i in ds:
    if i.dongia < min:
        i.dongia = min
print('==Thong tin sach giao khoa co don gai nho nhat: ')
for i in ds:
    if i.dongia == min:
        i.Xuat()
# sap xep danh sach giam dan theo sl
import operator
ds.sort(key=operator.attrgetter('sl'),reverse=True)
print('==Danh sach sau khi sap sep giam dan theo sl: ')
for i in range(0,n):
    ds[i].XuatSGK()
    print('\n')