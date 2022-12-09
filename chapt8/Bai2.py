from datetime import date
class Document:
    truong='Dh.SPKT Vĩnh Long'
    def __init__(self,ttl='',ncb='',nxb='',st=100):
        self.tentailieu=ttl
        self.nguoichubien=ncb
        self.namxuatban=nxb
        self.sotrang=st
    def Nhap(self):
        self.tentailieu= input("Nhap ten tai lieu")
        self.nguoichubien= input("Nhap ten chu bien")
        nxb= int(input("Nhap nam xuat ban: "))
        while nxb > date.today().year :
            nxb= int(input("Nhap lai nam xuat ban"))
        self.namxuatban=nxb
        st = int(input("Nhap so trang"))
        while st < 10 or st > 500:
            st= int(input("Nhap lai so trang"))
        self.sotrang=st
    def Xuat(self):
        print("Truong",self.truong)
        print("Ten tai lieu: ",self.tentailieu)
        print("Ten chu bien: ",self.nguoichubien)
        print("Nam xuat ban: ",self.namxuatban)
        print("So trang: ",self.sotrang)
    def Tentailieu(self):
        return self.tentailieu
    def Tenchubien(self):
        return self.nguoichubien
    def Namxuatban(self):
        return self.namxuatban
    def Sotrang(self):
        return self.sotrang

    def Sosanh(self,tl2):
        if self.sotrang > tl2.sotrang:
            return 1
        elif self.sotrang < tl2.sotrang:
            return  -1
        else:
            return 0

class Book(Document):
    def __init__(self,ttl='',ncb='',nxb='',st=100,ttcn='',nxban=''):
        super().__init__(ttl,ncb,nxb,st)
        self.ttchuyennganh=ttcn
        self.nhaxuatban=nxban
    def ChuyenNganh(self):
        return self.ttchuyennganh
    def NhaXuatBan(self):
        return self.nhaxuatban
    def NhapBook(self):
        print("Nhap thong tin sach: ")
        self.Nhap()
        self.ttchuyennganh=input("Nhap chuyen nganh: ")
        self.nhaxuatban = input("Nhap nha xuat ban: ")
    def XuatBook(self):
        print("Thong tin cua sach vua nhap la: ")
        self.Xuat()
        print("Chuyen Nganh : ",self.ttchuyennganh)
        print("Ten nha xuat ban: ",self.nhaxuatban)


class Magazine(Document):
    def __init__(self,ttl='',ncb='',nxb='',st=100,lv='',nn=''):
        super().__init__(ttl,ncb,nxb,st)
        self.linhvuc=lv
        self.ngonngu=nn
    def LinhVuc(self):
        return self.linhvuc
    def NgonNgu(self):
        return  seft.ngonngu
    def NhapTC(self):
        print("Nhap thong tap chi: ")
        self.Nhap()
        self.linhvuc=input("Nhap linh vuc: ")
        self.ngonngu = input("Nhap ngon ngu: ")

    def TimtapChimoinhat(self,tapchi1,tapchi2):
        if self.namxuatban > tapchi1.namxuatban and self.namxuatban> tapchi2. namxuatban :
            return 3
        elif tapchi1.namxuatban > self.namxuatban and tapchi1.namxuatban> tapchi2.namxuatban:
            return 4
        elif tapchi2.namxuatban> self.namxuatban and tapchi2.namxuatban  > tapchi1.namxuatban:
            return 5

#Tai lieu
'''dc1= Document()
dc1.Nhap()
dc1.Xuat()
print('\n')
dc2=Document()
dc2.Nhap()
dc2.Xuat()
print('\t')



if dc1.Sosanh(dc2)==1:
    print("So trang dc1 nhieu hon dc2")
elif dc1.Sosanh(dc2)==-1:
    print("So trang dc1 it hon dc2")
else:
    print("So trang dc1 bang dc2")
print('\n')

#Sach
book1=Book()
book1.NhapBook()
book1.XuatBook()
book2=Book()
book2.NhapBook()
book2.XuatBook()

if book1.Sosanh(book2)==1:
    print("Book 1 day hon book 2")
elif book1.Sosanh(book2)==-1:
    print("Book 2 day hon Book 1")
else:
    print("2 book bang nhau")
print('\n')


#Tap chi
tapchi1 = Magazine()
tapchi2 = Magazine()
tapchi3=Magazine()
tapchi1.NhapTC()
tapchi2.NhapTC()
tapchi3.NhapTC()

if tapchi1.TimtapChimoinhat(tapchi2,tapchi3) == 3:
    print("Tap chi 1 moi nhat ")
elif tapchi1.TimtapChimoinhat(tapchi2,tapchi3) == 4:
    print("Tap chi 2 moi nhat ")
elif tapchi1.TimtapChimoinhat(tapchi2,tapchi3) == 5:
    print("Tap chi 3 moi nhat ")
'''
print('\n')

ds=[]

n = int (input("Nhap vao so luong Sach: "))
while n<0 or n >100:
    n = int(input("Nhap lai so luong Sach: "))
for i in range (0,n):
    a=Book()
    a.NhapBook()
    ds.append(a)

for x in ds:
    x.XuatBook()
    print('\n')

NXB = input ("Nhap nha xuat ban muon dem: ")
dem = 0
for i in ds:
    if i.nhaxuatban.lower() == NXB.lower():
        dem=dem+1

print("Co ",dem ," sach cua NXB ",NXB)

Temp = Book()
for i in range (0,len(ds)-1):
    for j in range(1,len(ds)):
        if ds[i].sotrang > ds[j].sotrang:
            ds[i]= ds[j]
            ds[j]=Temp

d=0
for i in range(1,len(ds)):
    s=int(i.ttchuyennganh)!=""
    j=set(s)
print("co tat ca chuyen nganh:",len(j))

print("Danh sach sau khi sap xep lai: ")
for i in ds:
    i.XuatBook()