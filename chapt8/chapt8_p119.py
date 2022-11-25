class DaGiac:
    '''Định nghĩa lớp Đa giác'''
    def __init__(self, socanh):
        self.n = socanh
        self.canh = [0 for i in range(socanh)]

    def nhapcanh(self):
        self.canh = [float(input("Bạn hãy nhập giá trị cạnh "+str(i+1)+": ")) for i in range(self.n)]

    def hienthicanh(self):
        for i in range(self.n):
            print("Giá trị cạnh", i+1, "là", self.canh[i])

dg = DaGiac(4)
dg.nhapcanh()
dg.hienthicanh()

class TamGiac(DaGiac):
    '''Lớp Tam giác kế thừa lớp Đa giác'''
    def __init__(self):
        DaGiac.__init__(self, 3) # Có thể dùng lệnh supper

    def dientich(self):
        a, b, c = self.canh
        # Tính nửa chu vi
        p = (a+b+c)/2
        dt = (p*(p-a)*(p-b)*(p-c))**0.5
        print("Diện tích của hình tam giác là ", dt)

tg = TamGiac()
tg.nhapcanh()
tg.hienthicanh()
tg.dientich()
