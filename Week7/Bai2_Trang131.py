from datetime import date 
class Document:
    truong =  "ĐH.SPKT Vĩnh Long"
    def __init__(self,namedoc = "Tên tài liệu" , namecb = "Nguyễn Văn A" ,namxb = 1998, sotrang = 10 ):
        self.namedoc = namedoc
        self.namecb = namecb
        self.namxb = namxb
        self.sotrang = sotrang
    def Nhap(self):
        flag = False
        namht = date.today().year
        while flag == False:
            flag = True
            self.namedoc = input("Nhập tên tài liệu: ")
            self.namecb = input("Nhập người chủ biên: ")
            self.namxb = int(input("Nhập năm xuất bản: "))
            self.sotrang = int(input("Nhập số trang: "))
            if ((len(self.namedoc) == 0) or (len(self.namecb)==0) or (self.namxb > namht) or (self.sotrang<10 or self.sotrang > 500)):
                    flag = False
    def Xuat(self):
        print("Tên trường       : ",self.truong)
        print("Tên tài liệu     : ",self.namedoc)
        print("Người chủ biên   : ",self.namecb)
        print("Năm xuất bản     : ",self.namxb)
        print("Số trang         : ",self.sotrang)
    def TenDoc(self):
        return self.namedoc
    def TenCB(self):
        return self.namecb
    def Namxuatban(self):
        return self.namxb
    def Sotrang(self):
        return self.sotrang
    def Sosanh(self,Doc2):
        if self.sotrang > Doc2.sotrang:
            return 1
        elif self.sotrang < Doc2.sotrang:
            return -1
        else:
            return 0
class Book (Document) :
    def __init__(self,namedoc,namecb,namxb,sotrang,chuyennganh,tennxb):
        Document.__init__(self,namedoc,namecb,namxb,sotrang)
        self.chuyennganh = chuyennganh
        self.tennxb  = tennxb
    def NhapBook(self):
        Document.Nhap(self)
        self.chuyennganh = input("Nhập chuyên ngành: ")
        self.tennxb = input("Nhập vào tên nhà xuất bản: ")
    def XuatBook(self):
        Document.Xuat(self)
        print("Tên chuyên ngành: ",self.chuyennganh)
        print("Tên nhà xuất bản: ", self.tennxb)
    def ChuyenNganh(self):
        return self.chuyennganh
    def TenNXB(self):
        return  self.tennxb
    def SoSanhBook(self,Book2):
        if self.sotrang > Book2.sotrang:
            print("Quyển sách 1 dày hơn quyển sách 2")
        else:
            print("Quyển sách 2 dày hơn quyển sách 1")
class Magazine(Document):
    def __init__(self,namedoc,namecb,namxb,sotrang,linhvuc,ngonngu):
        Document.__init__(self,namedoc,namecb,namxb,sotrang)
        self.linhvuc = linhvuc
        self.ngonngu = ngonngu
    def NhapMagazine(self):
        self.ngonngu = input("Nhập ngôn ngữ: ")
        self.linhvuc = input("Nhập lĩnh vực: ")
    def Linhvuc(self):
        return self.linhvuc
    def Ngonngu(self):
        return self.ngonngu

# In danh sách Book vừa nhập được
Book_list = []
n = int(input("Nhập vào số lượng quyển sách: "))
while n < 0 or n > 100:
    n = int(input("Nhập vào số lượng quyển sách: "))
    print("Mời nhập danh sách gồm %d tài liệu: " % n)
    Book_list = []
for i in range(0, n):
    print("Nhập thông tin tài liệu %d: "%(i+1))
    temp = Book("Tên tài liệu", "Nguyễn Văn A", 1998, 10,"IT","EngLish")
    temp.NhapBook()
    Book_list.append(temp)
print("===DANH SÁCH %d TÀI LIỆU VỪA NHẬP=== "%(i+1))
for i in range(0,n):
    print("Thông tin tài liệu %d"%(i+1))
    Book_list[i].XuatBook()
# Đếm số sách được xuất bản bởi nhà xuất bản X
X = input("Nhập vào tên nhà xuất bản X: ")
dem = 0
for i in Book_list:
    if i.tennxb == X:
        dem +=1
print("Có ",dem,"quyển sách được xuất bản bởi nhà xuất bản",X)

# Cho biết các quyển sách đã nhập thuộc bao nhiêu chuyên ngành khác nhau
Book_Temp = []
for i in range(0,n):
    C_nganh = Book_list[i].ChuyenNganh()
    Book_Temp.append(C_nganh)
Set_Book  = set(Book_Temp)
print("Có ",len(Set_Book)," chuyên ngành khác nhau trong số các quyển sách")

# Sắp xếp các quyển sách tăng dần theo số trang và in ra danh sách sau khi sắp xếp
print("Thông tin sau khi được sắp xếp tăng dần ")
for i in range (0,n-1):
    for j in range(i+1,n):
        if Book_list[i].Sotrang() > Book_list[j].Sotrang():
            temp = Book_list[i]
            Book_list[i] = Book_list[j]
            Book_list[j] = temp
for i in range(0,n):
    print("Thông tin tài liệu %d"%(i+1))
    Book_list[i].XuatBook()



