class Person:
    quoctich = "Việt Nam"
    def __init__(self, hoten='', namsinh=0,gioitinh='',quequan=''):
        self.hoten = hoten
        self.namsinh = namsinh
        self.gioitinh = gioitinh
        self.quequan = quequan

    def Nhap(self):
        self.hoten = str(input("Nhap ho ten: "))
        self.namsinh = int(input("Nhap nam sinh: "))
        self.gioitinh = str(input("Nhap gioi tinh: "))
        self.quequan = str(input("Nhap que quan: "))

    def Xuat(self):
        print("- Quoc tich: ",Person.quoctich)
        print("- Ho ten: ", self.hoten)
        print("- Ngay sinh: ", self.namsinh)
        print("- Gioi tinh: ", self.gioitinh)
        print("- Que quan: ", self.quequan)

    def HoTen(self):
        return self.hoten

    def Namsinh(self):
        return self.namsinh

    def GioiTinh(self):
        return self.gioitinh

    def QueQuan(self):
        return self.quequan


class Staff(Person):
    def __init__(self,hoten='', namsinh=0,gioitinh='',quequan='',nambdlv=0, chuyenmon='', hsl=0, loaiNV=''):
        Person.__init__(self, hoten,namsinh,gioitinh,quequan)
        self.nambdlv = nambdlv
        self.chuyenmon = chuyenmon
        self.hsl = hsl
        self.loaiNV = loaiNV

    def NhapStaff(self):
        Person.Nhap(self)
        self.nambdlv = int(input("Nhap nam bat dau lam viec cua Staff: "))
        self.chuyenmon = str(input("Nhap chuyen mon cua Staff: "))
        self.hsl = float(input("Nhap vao he so luong cua Staff: "))
        self.loaiNV = str(input("Nhap vao loai nhan vien cua Staff: "))

    def XuatStaff(self):
        Person.Xuat(self)
        print("- Nam bat dau lam viec cua Staff:", self.nambdlv)
        print("- Chuyen mon cua Staff:", self.chuyenmon)
        print("- He so luong cua Staff:", self.hsl)
        print("- Loai nhan vien cua Staff:", self.loaiNV)

    def nambdlv(self):
        return self.nambdlv

    def ChuyenMon(self):
        return self.chuyenmon

    def HeSoLuong(self):
        return self.hsl

    def LoaiNV(self):
        return self.loaiNV

class Lecturer(Person):
    def __init__(self, hoten='', namsinh=0, gioitinh='', quequan='', nambdlv=0, chuyenmon='',trinhdo='', hsl=0):
        Person.__init__(self, hoten, namsinh, gioitinh, quequan)
        self.nambdlv = nambdlv
        self.chuyenmon = chuyenmon
        self.trinhdo = trinhdo
        self.hsl = hsl

    def NhapLecturer(self):
        Person.Nhap(self)
        self.nambdlv = int(input("Nhap nam bat dau lam viec cua Lecturer: "))
        self.chuyenmon = str(input("Nhap chuyen mon cua Lecturer: "))
        self.trinhdo = str(input("Nhap vao trinh do cua Lecturer: "))
        self.hsl = float(input("Nhap vao he so luong cua Lecturer: "))

    def XuatLecturer(self):
        Person.Xuat(self)
        print("- Nam bat dau lam viec cua Lecturer:", self.nambdlv)
        print("- Chuyen mon cua Lecturer:", self.chuyenmon)
        print("- Trinh do cua Lecturer:", self.trinhdo)
        print("- He so luong cua Lecturer:", self.hsl)

    def Nambdlvec(self):
        return self.nambdlv

    def Chuyenmon(self):
        return self.chuyenmon

    def TrinhDo(self):
        return self.trinhdo

    def HeSoLuongL(self):
        return self.hsl


class IT_Officers(Staff, Lecturer):
    khoa = 'CNTT'
    def __init(self, hoten='', namsinh=0,gioitinh='',quequan='',nambdlv=0, chuyenmon='', loaiNV='',trinhdo='', hsl=0, loaiCB=''):
        Staff.__init__(self, hoten, namsinh, gioitinh, quequan, nambdlv, chuyenmon, hsl, loaiNV)
        Lecturer.__init__(self, hoten, namsinh, gioitinh, quequan, nambdlv, chuyenmon, trinhdo, hsl)
        self.loaiCB = loaiCB

    def NhapIT(self):
        flag = True
        while flag:
            self.loaiCB = str(input("Nhap vao loai can bo: "))
            if self.loaiCB.upper() == 'STAFF' or self.loaiCB.upper() == 'LECTURER':
                flag = False
            else:
                print("Nhap sai. Yeu cua nhap lai.")
        if self.loaiCB.upper() == 'STAFF':
            Staff.NhapStaff(self)
        if self.loaiCB.upper() == 'LECTURER':
            Lecturer.NhapLecturer(self)

    def XuatIT(self):
        if self.loaiCB.upper() == 'STAFF':
            Staff.XuatStaff(self)
            print("- Loai can bo: ",self.loaiCB)
        if self.loaiCB.upper() == 'LECTURER':
            Lecturer.XuatLecturer(self)
            print("- Loai can bo: ",self.loaiCB)

    def TuoiCB(self):
        return 2022 - self.namsinh

    def NamCT(self):
        return 2022 - self.nambdlv

    def Luong(self):
        return self.hsl * 1490000

    def Swap(self, ob):
        if self.loaiCB.upper() == "STAFF":
            self.hoten, ob.hoten = ob.hoten, self.hoten
            self.namsinh, ob.namsinh = ob.namsinh, self.namsinh
            self.gioitinh, ob.gioitinh = ob.gioitinh, self.gioitinh
            self.quequan, ob.quequan = ob.quequan, self.quequan
            self.nambdlv, ob.nambdlv = ob.nambdlv, self.nambdlv
            self.chuyenmon, ob.chuyenmon = ob.chuyenmon, self.chuyenmon
            self.hsl, ob.hsl = ob.hsl, self.hsl
            self.loaiNV, ob.loaiNV = ob.loaiNV, self.loaiNV
        if self.loaiCB.upper() == "LECTURER":
            self.hoten, ob.hoten = ob.hoten, self.hoten
            self.namsinh, ob.namsinh = ob.namsinh, self.namsinh
            self.gioitinh, ob.gioitinh = ob.gioitinh, self.gioitinh
            self.quequan, ob.quequan = ob.quequan, self.quequan
            self.nambdlv, ob.nambdlv = ob.nambdlv, self.nambdlv
            self.chuyenmon, ob.chuyenmon = ob.chuyenmon, self.chuyenmon
            self.trinhdo, ob.trinhdo = ob.trinhdo, self.trinhdo
            self.hsl, ob.hsl = ob.hsl, self.hsl


ds=[]
flag = True
while flag:
    n = int(input("Nhap vao tong so nhan vien: "))
    if n < 0 or n > 50:
        print("Nhap sai. Yeu cau nhap lai.")
    else:
        flag = False
j = 1
for i in range (n):
    print("Nhap vao thong tin nhan vien thu ",j,":",sep='')
    j+=1
    temp = IT_Officers()
    temp.NhapIT()
    ds.append(temp)

j = 1
for i in ds:
    print("---------------------")
    print("Thong tin nhan vien thu ",j,":",sep='')
    j+=1
    i.XuatIT()

print("---------------------")
dem = 0
for i in ds:
    if i.NamCT() > 10:
        dem+=1
print("Co",dem,"nhan vien co tham nien tren 10 nam")
tuoiMax=0
for i in ds:
    if i.TuoiCB() > tuoiMax:
        tuoiMax = i.TuoiCB()
print("Ho ten nhan vien co tuoi lon nhat la: ",end='')
for i in ds:
    if i.TuoiCB() == tuoiMax:
        print(i.hoten)

for i in ds:
    for j in ds:
        if i.hsl < j.hsl:
            i.Swap(j)

j = 1
for i in ds:
    print("---------------------")
    print("Thong tin nhan vien thu ",j,":",sep='')
    j+=1
    i.XuatIT()


    

