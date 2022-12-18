from datetime import date
class HOCSINH():
    truong='THPT'
    def __init__(self, ht="", ns=date(2022, 12, 18), dtb=0):
        self.ht = ht.strip()
        self.ns = ns
        self.dtb = dtb

    def nhap(self):
        ht = input("Nhập Họ Tên: ")
        self.ht = ht.strip()
        checkns = False
        while checkns==False:
            ngay = int(input("Nhập Ngày sinh: "))
            while ngay < 0 or ngay > 32:
                ngay = int(input("Nhập lại Ngày sinh: "))
            thang = int(input("Nhập Tháng sinh: "))
            while thang < 0 or thang > 12:
                thang = int(input("Nhập lại Ngày sinh: "))
            nam = int(input("Nhập Năm sinh: "))
            while nam > date.today().year:
                ngay = int(input("Nhập lại Ngày sinh: "))
            try:
                self.ns = date(nam, thang, ngay)
                checkns = True
            except(ValueError):
                print("Ngày sinh không hợp lệ!!!")
                checkns = False
        dtb = float(input("Nhập điểm trung bình: "))
        while dtb < 0 or dtb > 10:
            dtb = float(input("Nhập lại điểm trung bình: "))
        self.dtb = dtb

    def Ten(self):
        ht = self.ht
        khoantrang = ht.rfind(' ')
        ten = self.ht[khoantrang+1:len(ht)]
        return ten

    def Tuoi(self):
        tuoi = date.today().year - self.ns.year
        return tuoi

    def xuat(self):
        print("Trường:", self.truong)
        print("Tên:", self.Ten())
        print("Tuổi:", self.Tuoi())
        print("Điểm trung bình:", self.dtb)

    def __add__(self, num):
        self.dtb += num
        return self.dtb

class HOCSINH_12(HOCSINH):
    khoi='12'
    def __init__(self, ht="", ns=date(2022, 12, 18), dtb=0, cmnd=''):
        super(HOCSINH_12, self).__init__(ht, ns, dtb)
        self.cmnd = cmnd
    def nhap(self):
        HOCSINH.nhap(self)
        self.cmnd = input("Nhập CMND: ")

    def Ho(self):
        ht = self.ht
        khoantrang = ht.find(' ')
        ho = self.ht[:khoantrang]
        return ho

    def xuat(self):
        HOCSINH.xuat(self)
        print("CMND:", self.cmnd)

HS1 = HOCSINH("Nguyễn Hữu Thọ", date(2003, 5, 26), 5)
HS1.nhap()
HS1.xuat()
print("HS sau khi được cộng điểm:", HS1.__add__(3))
print()

HS2 = HOCSINH_12("Nguyễn Kim Anh", date(2003, 11, 5), 9, 312541687)
# HS1.nhap()
HS2.xuat()
print('Họ:', HS2.Ho())
print()

N = int(input("Nhập vào N: "))
DSHS = []

for i in range(0, N):
    print(f"- Nhập THÔNG TIN HS {i+1}:")
    Obj = HOCSINH_12()
    Obj.nhap()
    DSHS.append(Obj)
    print()

print("===DANH SÁCH HỌC SINH: ")
for i in range(0, len(DSHS)):
    print(f'THÔNG TIN HS {i+1}:')
    Obj.xuat()
    print()

print("Họ tên HS có ĐTB nhỏ hơn 5: ")
for i in range(0, len(DSHS)):
    if(DSHS[i].dtb < 5):
        print(DSHS[i].ht)