from datetime import date
import operator
class SACH():
    def __init__(self, ms="", nn=date.today(), dg=0, sl=0, nxb=""):
        self.ms = ms
        self.nn = nn
        self.dg = dg
        self.sl = sl
        self.nxb = nxb

    def nhap(self):
        self.ms = input("Nhập Mã sách: ")
        ngay = input("Nhập Ngày nhập: ")
        thang = input("Nhập Tháng nhập: ")
        nam = input("Nhập Năm nhập")
        nn = date(nam, thang, ngay)
        self.nn = nn
        dg = input("Nhập Đơn giá: ")
        while dg < 0:
            dg = input("Nhập lại Đơn giá: ")
        self.dg = dg
        sl = input("Nhập Số lượng: ")
        while sl <0:
            sl = input("Nhập lại Số lượng: ")
        self.sl = sl
        self.nxb = input("Nhập NXB: ")

    def xuat(self):
        print("Mã sách: ", self.ms)
        print("Ngày nhập:", self.nn.strftime("%d/%m/%Y"))
        print("Đơn giá:", self.dg)
        print("Số lượng:", self.sl)
        print("NXB:", self.nxb)

class SACHGIAOKHOA(SACH):
    def __init__(self, ms="", nn=date.today(), dg=0, sl=0, nxb="", tt=""):
        super(SACHGIAOKHOA, self).__init__(ms, nn, dg, sl, nxb)
        self.tt = tt

    def nhap(self):
        SACH.nhap(self)
        tt = print("Nhập tình trạng (moi, cu): ")
        while tt != "moi" or tt != "cu":
            tt = print("Nhập lại Tình trạng (moi, cu): ")

    def xuat(self):
        SACH.xuat(self)
        print("Tình trạng:", end=" ")
        if(self.tt == "moi"):
            print("mới")
        elif(self.tt == "cu"):
            print("củ")

    def ThanhTien(self):
        if(self.tt=="moi"):
            return self.sl*self.dg
        elif(self.tt=="cu"):
            return self.sl*self.dg*0.5

class SACHTHAMKHAO(SACH):
    def __init__(self, ms="", nn=date.today(), dg=0, sl=0, nxb="", thue=0.0):
        super(SACHTHAMKHAO, self).__init__(ms, nn, dg, sl, nxb)
        self.thue = thue

    def nhap(self):
        SACH.nhap(self)
        thue = float(input("Nhập Số lượng: "))
        while thue < 0:
            thue = input("Nhập lại Số lượng: ")
        self.thue = thue
    def xuat(self):
        SACH.xuat(self)
        print("Thuế: ", self.thue)

    def ThanhTien(self):
        return self.sl*self.dg+float(self.thue)

SACH1 = SACH()
SACH1.xuat()
print()

SGK1 = SACHGIAOKHOA()
SGK1.xuat()
print("Thành tiền:", SGK1.ThanhTien())

STK1 = SACHTHAMKHAO()
STK1.xuat()
print("Thành tiền:", STK1.ThanhTien())
print()

L_NGK = []
# N = int(input("Nhập Số lượng sách giáo khoa: "))
# while N <= 0 or N >= 30:
#     N = int(input("Nhập lại Số lượng sách giáo khoa: "))
N = 3
L_NGK = [SACHGIAOKHOA("1", date(2022, 12, 1), 200, 2, "Đại học Cần Thơ", 'moi'),
        SACHGIAOKHOA("2", date(2022, 12, 2), 400, 5, "Đại học Cần Thơ", 'moi'),
        SACHGIAOKHOA("3", date(2022, 12, 2), 400, 5, "Đại học SPKT Vĩnh Long", 'moi'),
        SACHGIAOKHOA("4", date(2022, 12, 2), 200, 5, "Đại học SPKT Vĩnh Long", 'cu'),
         ]

TongThanhTien = 0
for i in range(len(L_NGK)):
    if L_NGK[i].nxb == "Đại học Cần Thơ":
        TongThanhTien += L_NGK[i].ThanhTien()

print("Tổng thành tiền: ", TongThanhTien)

min = L_NGK[0].dg
for i in range(1, len(L_NGK)):
    if L_NGK[i].dg < min:
        min = L_NGK[i].dg
print("Min:", min)

print("THÔNG TIN SÁCH CÓ ĐƠN GIÁ NHỎ NHẤT: ")
for i in range(0, len(L_NGK)):
    if L_NGK[i].dg == min:
        L_NGK[i].xuat()
        print()


L_NGK.sort(key=operator.attrgetter("sl"), reverse=True)

print("THÔNG TIN SGK GIẢM DẦN THEO SỐ LƯỢNG: ")
for i in range(len(L_NGK)):
    L_NGK[i].xuat()
    print()