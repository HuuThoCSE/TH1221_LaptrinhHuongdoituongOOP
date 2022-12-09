from datetime import date
class Sinhvien:
    truong = 'VLUTE'
    def __init__(self, mssv = '21004051', hoten = 'Tran Linh', ngaysinh = date(2007, 11, 11), dtb = 8.5):
        self.mssv = mssv
        self.hoten = hoten
        self.ngaysinh = ngaysinh
        self.dtb = dtb

    def Nhap (self):
        self.mssv = int(input('Nhập mssv: '))
        self.hoten = input('Nhập họ tên: ')
        ngay = int(input('Nhập ngày sinh: '))
        thang = int(input('Nhập tháng sinh: '))
        nam = int(input('Nhập năm sinh: '))
        self.ngaysinh = date (nam, thang, ngay)
        self.dtb = float(input('Nhập điểm trung bình: '))

    def Chuoicon(self):
        htt = self.hoten.strip()
        ktd = htt.find(' ')
        ho = htt[:ktd]

    def Tuoi (self):
        t = date.today().year - self.ngaysinh.year
        return t

    def Xuat(self):
        print('MSSV:', self.mssv)
        print('Họ tên:', self.hoten)
        print('Ngày sinh:', self.ngaysinh.strftime("%d%m%Y"))
        print('ĐTB:', self.dtb)

    #b
    def __add__(self, n):
        d = self.dtb + n
        return Sinhvien(self.mssv, self.hoten, self.ngaysinh, d)

    #c
class Sinhvien_IT(Sinhvien):
    khoa = 'FIT'
    def __init__(self, mssv = '21004051', hoten = 'Tran Linh', ngaysinh = date(2007, 11, 11), dtb = 8.5, qq = 'VL'):
        Sinhvien.__int__(self, mssv, hoten, ngaysinh, dtb)
        self.qq = qq

    def NhapIT (self):
        Sinhvien.Nhap(self)
        self.qq = input('Nhập quê quán: ')

    def ChuoiconIT(self):
        htt = self.hoten.strip()
        ktc = htt.find(' ')
        ten = htt[ktc+1:]
        return ten

    def XuatIT (self):
        Sinhvien.Xuat(self)
        print('Quê quán:', self.qq)

     #d
    def __lt__(self, other):
        if self.dtb < other.dtb:
            return True
        else:
            return False

sv1 = Sinhvien()
print('Thông tin sinh viên 1:')
sv1.Nhap()
print('Thông tin của sv1 là:')
sv1.Xuat()

h = float(input('Nhập vào 1 số thực: '))
print('Cộng số thực vào đtb là:', sv1.__add__(n=h))
sv1.Xuat()

print('Họ sv1:')
sv1.Chuoicon()

print('Tuổi sv1')
sv1.Tuoi()

sv2 = Sinhvien_IT()
print('Thông tin sinh viên 2:')
sv2.NhapIT()
print('Thông tin của sv2 là:')
sv2.XuatIT()

print('Tên sv2:')
sv2.ChuoiconIT()

if sv1.__lt__(sv2) == True:
    print('SV1 có điểm trung bình nhỏ hơn SV2.')
else:
    print('SV1 có điểm trung bình không nhỏ hơn SV2.')