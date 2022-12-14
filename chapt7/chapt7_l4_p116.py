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

A = Document('Anh va trinh', 'Nguyen Huu Tho', 2003, 42)
A.Xuat()
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
print("\n")

# ListSach = [["C++", "Bjarne Stroustrup", 1985, 230], ["SQL", "Donald D. Chamberlin", 1974, 340], ["Python", "Guido van Rossum", 1991,489], ["PHP", "Rasmus Lerdorf", 1995, 200]]

# N = int(input("Nhập Số lượng tài liệu: "))
# while N <= 0:
#     N = int(input("Nhập lại Số lượng tài liệu: "))
# N = 4

ListSach = []
N = 4
ListSach.append(Document("C++", "Bjarne Stroustrup", 1985, 230))
ListSach.append(Document("SQL", "Donald D. Chamberlin", 1974, 340))
ListSach.append(Document("Python", "Guido van Rossum", 1991,489))
ListSach.append(Document("PHP", "Rasmus Lerdorf", 1995, 200))

# for i in range(1, N+1):
#     Obj = Document()
#     Obj.Nhap()
#     ListSach.append(Obj)

print('=====DANH SACH SACH SAU KHI NHAP=====')
for x in ListSach:
    print(f"===THÔNG TIN SÁCH {x.TenTaiLieu}:")
    x.Xuat()
    print("\n")

dem = 0
for x in ListSach:
    if(x.SoTrang > 300):
        dem+=1

print(f"Có {dem} tài liệu có số trang trên 300\n")

# Cho biết tên chủ biên có nhiều tài liệu nhất
# for i in range(0, N):
#     for j in range(0, N):
#         if(ListSach[j].TenNguoiChuBien == ListSach[i].TenNguoiChuBien):
#             pass

cb = {} # Kieu DICT

# Khởi tạo giá trị => 0
for x in ListSach:
    if x.TenNguoiChuBien not in cb:
        cb[x.TenNguoiChuBien] = 0
# print(cb)

for x in ListSach:
    cb[x.TenNguoiChuBien] += 1
# print(cb)

max=0
for item in cb:
    if max < cb[item]:
        max = cb[item]
print(max)

print("=====DS có chủ biên có nhiều tài liệu nhất:")
for item in cb:
    if cb[item] == max:
        print("-", item)

# Sắp xếp danh sách tăng dần dựa vào số trang
import operator
ListSach.sort(key=operator.attrgetter('SoTrang'))
print("\n=====DANH SÁCH TĂNG DẦN THEO SỐ TRANG:")
for i in range(0, N):
    print(f"===THÔNG TIN SÁCH {i}:")
    ListSach[i].Xuat()
    print("\n")

ListSach.append(Document("Java", "James Gosling", 1995, 201))
ListSach.append(Document("Ruby", "Yukihiro Matsumoto", 2016, 220))
N+=2

#- Cach thu cong
for i in range(N-1):
    for j in range(i+1, N):
        if ListSach[i].NXB > ListSach[j].NXB:
            tam = ListSach[i]
            ListSach[i] = ListSach[j]
            ListSach[j] = tam

print("\n=====DANH SÁCH TĂNG DẦN THEO SỐ TRANG CÁCH 2:")
for x in ListSach:
    print(f"===THÔNG TIN SÁCH {x.TenTaiLieu}:")
    x.Xuat()
    print("\n")
