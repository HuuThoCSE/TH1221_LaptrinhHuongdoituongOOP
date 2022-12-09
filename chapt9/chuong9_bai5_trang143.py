from datetime import date
class SINHVIEN:
    truong = "VLUTE"
    def __init__(self, mssv=0, ho="", ten="", ngaysinh=date(2003, 1, 1), diemtrungbinh=0.0):
        self.MSSV = mssv
        self.Ho = ho
        self.Ten = ten
        self.HoTen = ho+' '+ten
        self.NgaySinh = ngaysinh
        self.DiemTrungBinh = diemtrungbinh

    def Nhap(self):
        self.MSSV = input("Nhập MSSV: ")
        self.Ho = input("Nhập Họ: ")
        self.Ten = input("Nhập Họ: ")
        self.HoTen = self.Ho+' '+self.Ten
        ngay = int(input("Nhập ngày sinh: "))
        thang = int(input("Nhập tháng sinh: "))
        nam = int(input("Nhập năm sinh: "))
        self.NgaySinh = date(nam, thang, ngay)
        self.DiemTrungBinh = float(input("Nhập điểm trung bình: "))

    def Xuat(self):
        print("Trường:", self.truong)
        print("MSSV:", self.MSSV)
        print("Họ:", self.Ho)
        print("Tên:", self.Ten)
        print("Tuổi:", date.today().year-self.NgaySinh.year)
        print("Ngày sinh:", self.NgaySinh.strftime("%d/%m/%Y"))
        print("Điểm trung bình:", self.DiemTrungBinh)

    def __add__(self, Number):
        self.DiemTrungBinh += Number
        return self.DiemTrungBinh

class SINHVIEN_IT(SINHVIEN):
    khoa = "FIT"
    def __init__(self, mssv=0, ho="", ten="", ngaysinh=date(2003, 1, 1), diemtrungbinh=0.0, quequan=""):
        SINHVIEN.__init__(self, mssv, ho, ten, ngaysinh, diemtrungbinh)
        self.QueQuan = quequan

    def Nhap(self):
        SINHVIEN.Nhap(self) # Chưa lấy dữ liệu ra
        self.QueQuan = input("Nhập Quê quán: ")

    def Xuat(self):
        SINHVIEN.Xuat(self)
        print("Quê quán:", self.QueQuan)

    def __lt__(self, SV2):
        if(self.DiemTrungBinh < SV2.DiemTrungBinh):
            return True
        else:
            return False

SV1 = SINHVIEN(21022008, "Nguyễn", "Hữu Thọ", date(2003, 5, 26), 3.0)
SV1.Xuat()

print(SV1.__add__(3))
print()

SV2 = SINHVIEN_IT(21022008, "Nguyễn", "Kim Anh", date(2003, 11, 5), 8.0, "Vĩnh Long")
# SV2.Nhap()
SV2.Xuat()

SV3 = SINHVIEN_IT(21022008, "Nguyễn", "Thị Hồng Ngát", date(2003, 8, 26), 9.0, "Hưng Yên")

if(SV2.__lt__(SV3)):
    print("Điểm trung bình SV1 nhỏ hơn SV2")
else:
    print("Điểm trung bình SV1 không nhỏ hơn SV2")