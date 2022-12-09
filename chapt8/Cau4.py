from datetime import date
class Person():
    '''Lop Person '''
    QuocTich = ' VietNam '
    def __init__(self, HT ='' , GT ='' ,QQ='',NS =date(2003,9,8)):
        self.Hoten = HT
        self.GioiTinh = GT
        self.Quequan = QQ
        self.Ngaysinh= NS
    def Nhap(self):
        self.Hoten = input("Nhap ho ten: ")
        self.Quequan = input("Nhap que quan: ")
        self.GioiTinh=input ("Nhap gioi tinh: ")
        ngay = int(input("Nhap ngay sinh: "))
        thang = int(input("Nhap thang sinh: "))
        nam = int(input ( " Nhap nam sinh: "))
        self.Ngaysinh = date(nam,thang,ngay)
    def Xuat(self):
        print("Quoc tich: ",Person.QuocTich)
        print("Ho ten: ",self.Hoten)
        print("Gioi tinh : ",self.GioiTinh)
        print("Que quan : ",self.Quequan )
        print("Ngay sinh : ",self.Ngaysinh.strftime("%d,%m,%Y"))
    def Hoten(self):
        return self.Hoten
    def Ngaysinh(self):
        return self.Ngaysinh
    def Gioitinh(self):
        return self.GioiTinh
    def Quequan(self):
        return self.Quequan
class Staff(Person):
    def __init__(self,NgayBD = date(2003,9,8),CM = '',HSL = '',LoaiNV = ' ',\
                 HT ='' , GT ='' ,QQ='',NS =date(2003,9,8)):
        super().__init__(HT,QQ,GT,NS)
        self.NgayBD = NgayBD
        self.ChuyenMon = CM
        self.HeSoLuong = HSL
        self.LoaiNV = LoaiNV
    def Nhap(self):
        print("Nhap thong tin nhan vien: ")
        ngay = int(input("Nhap ngay BD: "))
        thang = int(input("Nhap thang BD: "))
        nam = int(input(" Nhap nam Bd: "))
        self.NgayBD = date(nam, thang, ngay)
        self.ChuyenMon = input("Nhap chuyen mon: ")
        self.HeSoLuong = float(input("Nhap he so luong : "))
        self.LoaiNV = input ("Nhap loai Nhan vien : " )
    def Xuat(self):
        print("Thong tin Nhan vien vua nhap la: ")
        print("Ngay bat dau lam : ",self.NgayBD)
        print ("Chuyen Mon : ",self.ChuyenMon)
        print("He So luong : ",self.HeSoLuong)
        print("Thuoc loai NV: ",self .LoaiNV)
    def NgayBDL(self):
        return self.NgayBD
    def HSL(self):
        return self.HeSoLuong
class Lecturer (Person):
    def __init__(self,NgayBDlam=date(2003,8,9),ChuyenMon ='',TrinhDo='',HSL='',HangGV=''):
        self.NgayBDlam = NgayBDlam
        self.Chuyenmon=ChuyenMon
        self.Trinhdo = TrinhDo
        self.hangGV = HangGV
        self.HSL = HSL
    def Nhap(self):
        ngay = int(input("Nhap ngay BD lam: "))
        thang = int(input("Nhap thang BD lam : "))
        nam = int(input(" Nhap nam BD lam : "))
        self.NgayBDlam = date(nam, thang, ngay)
        self.Trinhdo = input ("Trinh do: ")
        self.HSL = float(input("Nhap he so luong :"))
    def Xuat(self):
        print("Ngay bat dau lam cua GV la : ",self.NgayBDlam)
        print("Trinh do cua GV la : ",self.Trinhdo)
        print("HSL la: ",self.HSL)
# class IT_Officers(Staff,Lecturer):
#     Khoa = 'CNTT'
#     def __init__(self):


ps1 = Person()
ps1.Nhap()
print("Thong tin Person1 la: ")
ps1.Xuat()

S1=Staff()
S1.Nhap()
S1.Xuat()

gv1= Lecturer()
gv1.Nhap()
gv1.Xuat()