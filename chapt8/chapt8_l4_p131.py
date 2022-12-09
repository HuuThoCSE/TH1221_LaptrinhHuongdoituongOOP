from datetime import date
class Person:
    quoctich = 'Việt Nam'
    def __init__(self, hoten='', ngaysinh=date(2022, 6, 22), gioitinh='', quequan=''):
        self.hoten = hoten
        self.ngaysinh = ngaysinh
        self.gioitinh = gioitinh
        self.quequan = quequan

    def nhap(self):
        self.hoten = input('Nhập họ tên: ')
        ngay = int(input('Nhập Ngày sinh: '))
        thang = int(input('Nhập Tháng sinh: '))
        nam = int(input('Nhập Năm sinh: '))
        self.ngaysinh = date(nam, thang, ngay)
        self.gioitinh = input('Nhập Giới tính: ')
        self.quequan = input('Nhập Quê quán: ')

    def xuat(self):
        print('Quoc tich: ', self.quoctich)
        print('Ho va ten: ', self.hoten)
        print('Ngay sinh: ', self.ngaysinh.strftime("%d/%m/%Y"))
        print('Gioi tinh: ', self.gioitinh)
        print('Que quan: ', self.quequan)

    def Hoten(self):
        return self.hoten

    def Ngaysinh(self):
        return self.ngaysinh.strftime("%d/%m/%Y")

    def Gioitinh(self):
        return self.gioitinh

    def Quequan(self):
        return self.quequan

class Staff(Person):
    def __init__(self, hoten='', ngaysinh=date(2022, 6, 22), gioitinh='', quequan='', startjob=date(2022, 2, 12), chuyenmon='', hesoluong=0, loainhanvien=''):
        Person.__init__(self, hoten, ngaysinh, gioitinh, quequan)
        self.startjob = startjob
        self.chuyenmon = chuyenmon
        self.hesoluong = hesoluong
        self.loainhanvien = loainhanvien

    def nhap(self):
        Person.nhap(self)
        print("===NGAY LAM VIEC: ")
        ngay = int(input("- Ngay: "))
        thang = int(input("- Thang: "))
        nam = int(input("- Nam: "))
        self.startjob = date(nam, thang, ngay)
        self.chuyenmon = input("Nhap Chuyen mon: ")
        self.hesoluong = input("Nhap He so luong: ")
        self.loainhanvien = input("Nhap Loai nhan vien: ")

    def xuat(self):
        print("===STAFF:")
        Person.xuat(self)
        print("Ngay lam viec: ", self.startjob.strftime("%d/%m/%Y"))
        print("Chuyen mon: ", self.chuyenmon)
        print('He so luong: ', self.hesoluong)
        print('Loai nhan vien: ', self.loainhanvien)

    def Startjob(self):
        return self.startjob.strftime("%d/%m/%Y")

    def Hesoluong(self):
        return self.hesoluong

class Lecturer(Person):
    def __init__(self, hoten='', ngaysinh=date(2022, 6, 22), gioitinh='', quequan='', startjob=date(2022, 2, 12), chuyenmon='', trinhdo='', hesoluong=0, hangiangvien=3):
        Person.__init__(self, hoten, ngaysinh, gioitinh, quequan)
        self.startjob = startjob
        self.chuyenmon = chuyenmon
        self.trinhdo = trinhdo
        self.hesoluong = hesoluong
        self.hangiangvien = hangiangvien

    def xuat(self):
        print("===Lecturer:")
        Person.xuat(self)
        print("Ngay lam viec: ", self.startjob.strftime("%d/%m/%Y"))
        print("Chuyen mon: ", self.chuyenmon)
        print('He so luong: ', self.hesoluong)
        print('Hang giang vien: ', self.hangiangvien)

    def Startjob(self):
        return self.startjob

    def Trinhdo(self):
        return self.trinhdo

    def Hesoluong(self):
        return self.hesoluong

class IT_Officers(Staff, Lecturer):
    khoa = 'CNTT'
    def __init__(self, hoten, ngaysinh, gioitinh, quequan, startjob, hesoluong, chuyenmon, loaicanbo):
        super(IT_Officers, self).__init__(hoten, ngaysinh, gioitinh, quequan, startjob, hesoluong, chuyenmon)
        self.loaicanbo = loaicanbo

    def nhap(self):
        Person.nhap(self)
        print("===NGAY LAM VIEC: ")
        ngay = int(input("- Ngay: "))
        thang = int(input("- Thang: "))
        nam = int(input("- Nam: "))
        self.startjob = date(nam, thang, ngay)
        self.chuyenmon = input("Nhập Chuyên môn: ")
        self.hesoluong = float(input("Nhập Hệ số lương: "))
        self.loaicanbo = int(input('Nhập Loại cán bộ: ')) # 1- Hoàn thành xuất sắc nhiệm vụ; 2- Hoàn thành tốt nhiệm vụ; 3- Hoàn thành nhiệm vụ nhưng còn hạn chế về năng lực (đối với cán bộ, công chức); hoàn thành nhiệm vụ (đối với viên chức); 4- Không hoàn thành nhiệm vụ.

    def xuat(self):
        Person.xuat(self)
        print('KHOA:', self.khoa)
        print('Loại cán bộ:', self.loaicanbo)

    def Tuoi(self):
        return date.today().year-self.ngaysinh.year

    def Luong(self):
        return int(self.hesoluong)*1490000

    def SoNamCongTac(self):
        return date.today().year-self.startjob.year

Nguoi1 = Person()
Nguoi1.xuat()
print()
Nguoi1 = Person('Nguyen Van A', date(2003, 5, 26), 'nam', 'Tien Giang')
Nguoi1.xuat()
print()

print(Nguoi1.Hoten())
print(Nguoi1.Ngaysinh())
print(Nguoi1.Gioitinh())
print(Nguoi1.Quequan())
print()


print("Module STAFF")
Nguoi2 = Staff()
Nguoi2.xuat()
Nguoi2 = Staff('Nguyen Huynh N', date(2003, 3, 30), 'nu', 'Vinh Long', date(2022, 2, 12), 'Ke toan', 0, 'VIP')
Nguoi2.xuat()
print()

print("Module LETURER")
Nguoi3 = Lecturer()
Nguoi3.xuat()
Nguoi3 = Lecturer('Le Kim A', date(1978, 5, 20), 'nam', 'Vinh Long', date(2007, 2, 12), 'CNTT', 'Thac si', 5, 3)
Nguoi3.xuat()
print()

print("CLASS IT_Officers")
Nguoi5 = IT_Officers('Nguyen Dai P', date(2003, 5, 26), 'nam', 'Tien Giang', date(2018, 2, 12), "CNTT", 3.14, 1)
# Nguoi5.nhap()
Nguoi5.xuat()
print("Tuoi: ", Nguoi5.Tuoi())
print("Số năm công tác: ", Nguoi5.SoNamCongTac())
print("Luong: ", Nguoi5.Luong())
print()

# N = int(input('Nhập N: '))
# while N < 0 or N > 50:
#     N = int(input('Nhập N: '))
# List_IT_Officers = []
# for i in range(1, N+1):
#     Obj = IT_Officers()
#     Obj.nhap()