#NguyenThiBichNgoc_21022021_De3_May21
from datetime import date
class HOCVIEN:
    def __init__(self, mshv='', hoten='',ngaysinh=date(2003,1,9),diemthi=10):
        self.mshv=mshv
        self.ht=hoten
        self.ns=ngaysinh
        self.dt=diemthi
    def Nhap(self):
        self.mshv=input('ma so hoc vien:  ')
        self.ht=input('ho ten: ')
        ngay=int(input('ngay sinh: '))
        thang=int(input('thang sinh: '))
        nam=int(input('nam sinh: '))
        self.ns=date(nam,thang,ngay)
        self.dt=float(input('diem thi: '))
    def Xuat(self):
        print('ma so hoc vien: ', self.mshv)
        print('ho ten:  ', self.ht)
        print('ngay sinh: ',self.ns.strftime("%d/%m/%y"))
        print('diem thi: ',self.dt)
    def mshv(self):
        return self.mshv
    def ht(self):
        return self.ht
    def ngaysinh(self):
        return self.ns
    def diemthi(self):
        return self.dt
    def __add__(self,n):
        x=self.dt+float(n)
        return x
    def Chuoicon(self):
        a = self.ht.split()
        return a[len(a) - 1]
class HOCVIEN_NC(HOCVIEN):
    trinhdo='NC'
    def __init__(self, mshv='', hoten='',ngaysinh=date(2003,1,9),diemthi=10,sdt=''):
        super().__init__()
        self.sdt=sdt
    def Nhap(self):
        HOCVIEN.Nhap(self)
        self.sdt=input('so dien thoai: ')
    def Xuat(self):
        print('ma so hoc vien: ', self.mshv)
        print('ho ten:  ', self.ht)
        print('ngay sinh: ',self.ns.strftime("%d/%m/%y"))
        print('diem thi: ',self.dt)
        print('so dien thoai: ',self.sdt)
    def Ngaysinh(self):
        return self.ns.day

'''A=HOCVIEN()
print('---nhap thong tin hoc vien---')
A.Nhap()
A.Xuat()
print('ten cua hoc vien nay la: ',A.Chuoicon())
n= float(input('nhap so thuc bat ky: '))
print('diem sau khi duoc cong la: ',A.__add__(n))'''

B=HOCVIEN_NC()
print('---nhap thong tin hoc vien NC---')
B.Nhap()
B.Xuat()

n = int(input('nhap so luong hoc vien: '))
while n <= 0:
    n = int(input('nhap so luong hoc vien: '))
ds = []
for i in range(n):
    print('nhap hoc vien thu ', i+1,': ')
    C=HOCVIEN_NC
    C.Nhap()
    ds.append(C)
print('danh sach cac thong tin vua nhap la: ')
for i in range(n):
    ds[i].Xuat()
d = 0
for i in range(n):
    if ds[i].Ngaysinh == 5 or ds[i].Ngaysinh == 15 or ds[i].Ngaysinh == 25:
        d += 1
print('co ',d,' hoc vien sinh vao ngay 5,15,25')
print("Ten cua cac hoc vien co so dien thoai bat dau la '0907': ")
for i in ds:
    kt= i.sdt.find('0907',0,4)
    if kt ==0:
        print(i.ht)
print()
for i in range(n - 1):
    for j in range(i + 1, n):
        if ds[i].diemthi() > ds[j].diemthi():
            ds[i], ds[j] = ds[j], ds[i]
print('danh sach hoc vien sau khi sap xep giam dan theo diem thi la: ')
for i in range(n):
    ds[i].Xuat()