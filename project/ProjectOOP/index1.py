# https://www.studocu.com/vn/document/truong-dai-hoc-mo-ha-noi/tin-dai-cuong/bai-tap-lon-lap-trinh-huong-doi-tuong/19643678
class Nguoi():
    def __init__(self, hoten: str, quequan: str, namsinh: int, gioitinh: str):
        self.hoten = hoten
        self.quequan = quequan
        self.namnsinh = namsinh
        self.gioitinh = gioitinh

    def Nhap(self):
        self.hoten = input("Nhập Họ tên: ")
        self.quequan = input("Nhập Quê quán: ")
        self.namnsinh = input("Nhập Năm sinh: ")
        self.gioitinh = input(("Nhập Giới tính: 0"))

    def Hien(self):
        print("Họ tên:", self.hoten)
        print("Quê quán:", self.quequan)
        print("Năm sinh:", self.namnsinh)
        print("Giới tính:", self.gioitinh)

class NguyenVong():
    def __init__(self, maNganh: str, maTruong: str, khoiXT, str, maNv: int, diemthi: float):
        self. maNganh = maNganh
        self.maTruong = maTruong
        self.khoiXT = khoiXT
        self.maNv = maNv
        self.diemthi = diemthi

    def nhapNguyenVong(self):
        self.maNganh = print("Nhập Mã ngành: ")
        self.maTruong = print("Nhập Mã trường: ")
        self.khoiXT = print("Nhập Khối xét tuyển: ")
        self.maNv = print("Nhập Mã nguyện vọng: ")
        self.diemthi = print('Nhập Điểm thi: ')

    def hienNguyenVong(self):
        print("Mã ngành:", self.maNganh)
        print("Mã trường:", self.maTruong)
        print("Khối xét tuyển:", self.khoiXT)
        print("Mã nguyện vọng:", self.maNv)
        print("Điểm thi:",self.diemthi)

class ThiSinh(Nguoi, NguyenVong):
    def __init__(self, hoten: str, quequan: str, namsinh: int, gioitinh: str, SBD: str, diemuutien: float, nguyenvong: list):
        super(ThiSinh, self).__init__(hoten, quequan, namsinh, gioitinh)
        self.SBD = SBD
        self.diemUuTien = diemuutien
        self.NguyenVong = nguyenvong

    def Nhap(self):
        ThiSinh.Nhap(self)
        self.SBD = input("Nhập SBD: ")
        self.diemUuTien = input("Nhập Điểm ưu tiên: ")
        self.NguyenVong = input("Nhập Nguyện Vong: ")

    def Hien(self):
        Nguoi.Hien(self)
        print("Số báo danh:", self.SBD)
        print("Điểm ưu tiên:", self.diemUuTien)
        print("Nguyện vọng:", self.NguyenVong)

    def nhapDSNguyenVong(self):
        NguyenVong.nhapNguyenVong(self)

    def hienDSNguyenVong(self):
        NguyenVong.hienNguyenVong(self)

    def hienThongTinTS(self):
        print("SBD:", self.SBD)
        print("Điểm ưu tiên:", self.diemUuTien)

class GiamThi(Nguoi):
    def __init__(self, hoten: str, quequan: str, namsinh: int, gioitinh: str, maGT: str, donviCT: str):
        super(GiamThi, self).__init__(hoten, quequan, namsinh, gioitinh)
        self.maGT = maGT
        self.donviCT = donviCT

    def Nhap(self):
        Nguoi.Nhap(self)
        self.maGT = input("Nhập mã GT: ")
        self.donviCT = input("Nhập Đơn vị công tác: ")

    def Hien(self):
        Nguoi.Hien(self)
        print("Mã Giám thị:", self.maGT)
        print("Đơn vị công tác", self.donviCT)

class QuanLy():
    pass

TS1 = ThiSinh("Nguyễn Hữu Thọ ", "Tiền Giang", 2003, "nam", "21022008", 3.5, [("CTT", "VLU", "A0", "deoco", 8.0), ("KMT", "VLU", "A0", "deoco", 9.0)])
TS1.Hien()
print()

GT1 = GiamThi("Nguyễn Văn Hiếu", "Hog biết", 1968, "nam", "GT1", "VLU")
GT1.Hien()