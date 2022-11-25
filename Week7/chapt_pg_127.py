class HinhChuNhat:
    '''Định nghĩa lớp Hình chữ nhật'''
    def __init__(self, sc):
        self.n = sc
        self.canh = [0 for i in range(sc)]

    def nhap(self):
        self.canh = [float(input("Nhập giá trị cạnh "\
                                 +str(i+1)+": ")) for i in range(self.n)]

    def xuat(self):
        for i in range(self.n):
            print("Giá trị cạnh", i+1, "là", self.canh[i])

    def dientich(self):
        cd = self.canh[0]
        cr = self.canh[1]
        dt = cd * cr
        return dt

class HinhVuong(HinhChuNhat):
    '''Lớp Hình vuông kế thừa lớp Hình chữ nhật
    và ghi đè phương thức tạo và tính diện tích'''
    def __init__(self):
        super().__init__(1)

    def dientich(self):
        a = self.canh[0]
        return a*a
print("Làm việc với hình chữ nhật: ")
hcn = HinhChuNhat(2)
hcn.nhap()
hcn.xuat()
print("Diện tích = ", hcn.dientich())
print("Làm việc với hình vuông: ")
hv = HinhVuong()
hv.nhap()
hv.xuat()
print("Diện tích = ", hv.dientich())