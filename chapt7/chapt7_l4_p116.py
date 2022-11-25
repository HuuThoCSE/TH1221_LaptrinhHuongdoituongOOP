from datetime import date
class Document:
    truong = 'DH.SPKT Vĩnh Long'
    def __init__(self, TenTaiLieu="", TenNguoiChuBien="", NXB="", SoTrang=0):
        self.TenTaiLieu = TenTaiLieu
        self.TenNguoiChuBien = TenNguoiChuBien
        self.NXB = NXB
        self.SoTrang = SoTrang

    def Nhap(self):
        self.TenTaiLieu = input('Nhập tên tài liệu: ')
        self.TenNguoiChuBien = input('Nhập tên người chủ biên: ')

        self.NXB = int(input('Nhập năm xuất bản: '))
        while self.NXB > date.today().year:
            self.NXB = int(input('Nhập lại năm xuất bản: '))

        self.SoTrang = int(input("Nhập số trang: "))
        while 10 > self.SoTrang or self.SoTrang > 500:
            self.SoTrang = int(input("Nhập lại số trang: "))

    def Xuat(self):
        print("Tên trường:", self.truong)
        print("Tên Tài liệu:", self.TenTaiLieu)
        print("Tên Người chủ biên:", self.TenNguoiChuBien)
        print("Năm xuất bản", self.NXB)
        print("Số trang:", self.SoTrang)

    def InTenTaiLieu(self):
        print('Tên tài liệu:', self.TenTaiLieu)

    def SoSanhSoTrang(self, Sach2):
        if(self.SoTrang > Sach2.SoTrang):
            return 1
        elif self.SoTrang < Sach2.SoTrang:
            return -1
        else:
            return 0

A = Document('Anh va trinh', 'Nguyen Huu Tho', 2003, 42)
# A.Nhap()
A.Xuat()
A.InTenTaiLieu()

B = Document('Chi va em', 'Nguyen Kim Anh', 2022, 42)
# B.Nhap()
# B.InTenTaiLieu()

if(A.SoSanhSoTrang(B)==1):
    print("Sách 1 nhiều trang hơn Sách 2.")
elif(A.SoSanhSoTrang(B)==-1):
    print("Sách 2 nhiều trang hơn Sách 1.")
else:
    print("Sách 1 và Sách 2 có số trang bằng nhau.")

# ListSach = [["C++", "Bjarne Stroustrup", 1985, 230], ["SQL", "Donald D. Chamberlin", 1974, 340], ["Python", "Guido van Rossum", 1991,489], ["PHP", "Rasmus Lerdorf", 1995, 200]]
#
# # N = int(input("Nhập N: "))
# N = 4]
ListSach = []
ListSach.append(Document("C++", "Bjarne Stroustrup", 1985, 230))
ListSach.append(Document("SQL", "Donald D. Chamberlin", 1974, 340))
ListSach.append(Document("Python", "Guido van Rossum", 1991,489))
ListSach.append(Document("PHP", "Rasmus Lerdorf", 1995, 200))
# N = int(input("Nhập N: "))
N = 4
# for i in range(1, N+1):
#     Obj = Document()
#     Obj.Nhap()
#     print('===============')
#     ListSach.append(Obj)

for i in range(0, N):
    print(f"===THÔNG TIN SÁCH {i}:")
    ListSach[i].Xuat()

dem = 0
for i in range(0, N):
    if(ListSach[i].SoTrang > 300):
        dem+=1

print(f"Có {dem} tài liệu có số trang trên 300")

# Cho biết tên chủ biên có nhiều tài liệu nhất
# for i in range(0, N):
#     for j in range(0, N):
#         if(ListSach[j].TenNguoiChuBien == ListSach[i].TenNguoiChuBien):
#             pass


# Xắp xếp danh sách tăng dần dựa vào số trang
import operator
ListSach.sort(key=operator.attrgetter('SoTrang'))
print("=====DANH SÁCH TĂNG DẦN THEO SỐ TRANG:")
for i in range(0, N):
    print(f"===THÔNG TIN SÁCH {i}:")
    ListSach[i].Xuat()

