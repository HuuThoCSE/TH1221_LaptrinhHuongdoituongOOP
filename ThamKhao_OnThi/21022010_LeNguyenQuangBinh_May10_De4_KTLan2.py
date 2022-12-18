#Lê Nguyễn Quang Bình, 21022010, Đề 4, Máy 10
from datetime import date
class NGUOI_HOC:
    def __init__(self,mssv=0,hoten='',ngaysinh='1/1/2000',diemthi=0):
        self.msv=mssv
        self.ht=hoten
        temp=ngaysinh.split('/')
        self.ns=date(int(temp[2]),int(temp[1]),int(temp[0]))
        self.dt=diemthi
    def Nhap(self):
        self.msv=input('Nhập mã số sinh viên: ')
        self.ht=input('Nhập họ tên: ')
        ngay=int(input('Nhập ngày sinh: '))
        thang=int(input('Nhập tháng sinh:'))
        nam=int(input('Nhập nam sinh: '))
        self.ns=date(nam,thang,ngay)
        self.dt=float(input('Nhập điểm thi: '))
    def ChuoiCon(self):
        a=self.ht.split()
        return a[len(a)-1]
    def Xuat(self):
        print('MSSV:',self.msv,'\tHọ tên:',self.ht)
        print('Ngày sinh:',self.ns.strftime('%d/%m/%Y'),'\tĐiểm thi:',self.dt)
    def __sub__(self, n):
        self.dt-=n
        if self.dt<0:
            self.dt=0.0
class NGUOI_HOC_CB(NGUOI_HOC):
    TrinhDo='CB'
    def __init__(self,mssv=0,hoten='',ngaysinh='1/1/2000',diemthi=0,sodienthoai=''):
        super().__init__(mssv,hoten,ngaysinh,diemthi)
        self.sdt=sodienthoai
    def Nhap(self):
        NGUOI_HOC.Nhap(self)
        self.sdt=input('Nhập số điện thoại: ')
    def Xuat(self):
        print('Trình độ:',self.TrinhDo)
        NGUOI_HOC.Xuat(self)
        print('Số điện thoại:',self.sdt)
A=NGUOI_HOC()
print('--Nhập thông tin sinh viên--')
A.Nhap()
print('\n--Sinh viên:',A.ChuoiCon())
A.Xuat()
n=float(input('Nhập số điểm cần thi trừ: '))
print('--Sinh viên:',A.ChuoiCon())
A-n
A.Xuat()
#B=NGUOI_HOC_CB(123,'Anh A','7/7/2007',12,'0123')
B=NGUOI_HOC_CB()
print('**Nhập thông tin sinh viên có trình độ CB**')
B.Nhap()
print('\n--Sinh viên:',B.ChuoiCon())
B.Xuat()
n=float(input('Nhập số điểm cần thi trừ: '))
B-n
print('\n--Sinh viên:',B.ChuoiCon())
B.Xuat()

DS=[]
nds=int(input('\nNhập số lượng sinh viên: '))
for i in range(nds):
    print('###Nhập sinh viên thứ',i+1,'###')
    T=NGUOI_HOC_CB()
    T.Nhap()
    DS.append(T)
print('@@@Danh sách sinh viên@@@')
for i in DS:
    print('==================================')
    i.Xuat()
dem=0
quy2=[4,5,6]
for i in DS:
    if i.ns.month in quy2:
        dem+=1
print('Số lượng người học sinh vào quý 2=',dem)
print('Học sinh có số điện thoại đầu là "0919":')
for i in DS:
    if i.sdt[:4]=='0919':
        print(i.ChuoiCon())
for i in range(nds-1):
    for j in range(i,nds):
        if DS[i].dt>DS[j].dt:
            DS[i],DS[j]=DS[j],DS[i]
print('@@@Danh sách sinh viên@@@')
for i in DS:
    print('==================================')
    i.Xuat()
#Lê Nguyễn Quang Bình, 21022010, Đề 4, Máy 10