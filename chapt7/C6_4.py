from _datetime import date
class Document:
    truong="DH.SPKT Vinh Long"
    def __init__(self, tl=" ", cb=" ", nxb=2021, st=100):
        self.tl = tl
        self.cb = cb
        self.nxb = nxb
        self.st = st

    def Nhap(self):
        self.tl = input("Tên tài liệu: ")
        self.cb = input("Tên người chủ biên: ")
        self.nxb = int(input("Năm sản xuất: "))
        self.st = int(input("Số trang: "))

        # Ràng buộc năm xuất bản
        while self.nxb > date.today().year:
            self.nxb = int(input("Vui lòng nhập lại năm xuất bản: "))

        # Ràng buộc số trang
        while self.st < 10 or self.st > 500:
            self.st = int(input("Vui lòng nhập lại số trang: "))

    def Xuat(self):
        print("Truong ",self.truong)
        print("Ten tai lieu : ",self.tl)
        print("Ten nguoi chu bien : ", self.cb)
        print("Nam xuat ban : ", self.nxb)
        print("So trang : ",self.st)

    def Tentailieu(self):
        return self.tl

    def Tenchubien(self):
        return self.cb

    def Namxuatban(self):
        return self.nxb

    def Sotrang(self):
        return self.st

# So sánh số trang
    def Sosanh(self, tl2):
        if self.st > tl2.st:
            return 1
        elif self.st < tl2.st:
            return -1
        else:
            return 0

        # Gọi các hàm trong lớp class Document
        dc1.Document()
        dc1.Xuat()
        dc1.Nhap()

        dc2.Document()
        dc2.Nhap()
        dc2.Xuat()


        # So sánh số trang dc1 và dc2
        if dc1.sosanh(dc2) == 1:
            print("Số trang dc1 nhiều hơn dc2.")
        elif dc1.Sosanh(2) == -1:
            print("Số trang dc1 ít hơn dc2.")
        else:
            print("Số trang dc1 bằng dc2.")

# Tạo 1 ds rỗng để chứa N tài liệu
ds = []
N = int(input("Nhập vào N số lượng tài liệu: "))

for i in range(N):
    dc = Document()
    dc.Nhap()
    ds.append(dc)

for x in ds:
    x.Xuat()

# Đếm số tài liệu có số trang lớn hơn 300
dem = 0
for i in ds:
    if i.st() > 300:
        dem += 1
print("Số lượng tài liệu có số trang >300 là: ", dem)

# Chủ biên có nhiều tài liệu nhất
max = 0
for item in Document.cb:
    if max < Document.cb[item]:
        max = Document.cb[item]
print(max)

print("Danh sách chủ biên có nhiều tài liệu nhất:")
for item in Document.cb:
    if Document.cb[item] == max:
        print(item)

# Sắp xếp tăng dần theo năm xuất bản:
for i in range(N-1):
    for j in range(i+1, N):
        if ds[i].nxb > ds[j].nxb:
            tam = ds[i]
            ds[i] = ds[j]
            ds[j] = tam
print("DS sau khi sx tăng dần theo năm xb:")
for x in ds:
    x.Xuat()