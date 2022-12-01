from datetime import date
class Document:
    truong = 'DH.SPKT Vĩnh Long'
    def __init__(self, TenTaiLieu="", TenNguoiChuBien="", NXB=2022, SoTrang=0):
        self.TenTaiLieu = TenTaiLieu
        self.TenNguoiChuBien = TenNguoiChuBien
        self.NXB = NXB
        self.SoTrang = SoTrang

    def Nhap(self):
        self.TenTaiLieu = input('Nhập tên tài liệu: ')
        self.TenNguoiChuBien = input('Nhập tên người chủ biên: ')

        NXB = int(input('Nhập năm xuất bản: '))
        while NXB > date.today().year:
            NXB = int(input('Nhập lại năm xuất bản: '))
        self.NXB = NXB

        SoTrang = int(input("Nhập số trang: "))
        while 10 > SoTrang > 500:
            SoTrang = int(input("Nhập lại số trang: "))
        self.SoTrang = SoTrang

    def Xuat(self):
        print("Tên trường:", self.truong)
        print("Tên Tài liệu:", self.TenTaiLieu)
        print("Tên Người chủ biên:", self.TenNguoiChuBien)
        print("Năm xuất bản", self.NXB)
        print("Số trang:", self.SoTrang)

    def InTenTaiLieu(self):
        print('Tên tài liệu:', self.TenTaiLieu, "\n")

    def SoSanhSoTrang(self, Sach2):
        if(self.SoTrang > Sach2.SoTrang):
            return 1
        elif self.SoTrang < Sach2.SoTrang:
            return -1
        else:
            return 0

class Book(Document):
    def __init__(self, ChuyenNganh="", TenNXB=""):
        super().__init__(self)
        self.ChuyenNganh = ChuyenNganh
        self.TenNXB = TenNXB
    def Xuat(self):
        print("=====BOOK:")
        Document.Xuat(self)
        print("Chuyên ngành:", self.ChuyenNganh)
        print("Tên Nhà xuất bản:", self.TenNXB)

    def ValueChuyenNganh(self):
        return self.ChuyenNganh

    def ValueTenNXB(self):
        return self.TenNXB

class Magazine(Document):
    def __int__(self, TenTaiLieu, TenNguoiChuBien, NXB, SoTrang, LinhVuc, NgonNgu):
        Document.__init__(self, TenTaiLieu, TenNguoiChuBien, NXB, SoTrang)
        self.LinhVuc = LinhVuc
        self.NgonNgu = NgonNgu

    def Nhap(self):
        Document.Nhap(self)
        self.LinhVuc = input("Lĩnh vực: ")
        self.NgonNgu = input("Ngôn ngữ: ")

    def Xuat(self):
        print("=====Magazine: ")
        Document.Xuat(self)
        print("Lĩnh vực:", self.LinhVuc)
        print("Ngôn ngữ:", self.NgonNgu)

    def ValueLinhVuc(self):
        return self.LinhVuc

    def ValueNgonNgu(self):
        return self.NgonNgu

Doc = Document()
# Doc.Xuat()
# Doc.Nhap()
Doc.Xuat()
print()

Book1 = Book()
Book1.Xuat()
# Book1.Nhap()
# Book1.Xuat()
print()

Magazine1 = Magazine("Bao khoa hoc","Nguyen Huu Tho", 2022, 30,"CNTT", "TiengViet")
# Magazine1 = Magazine()
# Magazine1.Nhap()
Magazine1.Xuat()