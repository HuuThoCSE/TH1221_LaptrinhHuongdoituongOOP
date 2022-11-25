import math
class Function:
    def __init__(self, tuso, mauso):
        self.tuso = tuso
        self.mauso = mauso

    def Nhap(self):
        self.tuso = int(input('Nhập tử số: '))
        self.mauso = int(input('Nhập mẫu số: '))
        while self.mauso == 0:
            self.tuso = int(input('Nhập tử số: '))
            self.mauso = int(input('Nhập mẫu số (ms > 0): '))

    def Xuat(self):
        if self.mauso < 0 and self.tuso > 0:
            print(-self.tuso,"/",self.mauso)
        elif self.mauso < 0 and self.tuso < 0:
            print(abs(self.tuso,"/",self.mauso))
        elif self.tuso == 0:
            print(0)
        elif self.mauso == 1:
           print(self.tuso)

    def Tuso(self):
        return self.tuso

    def Mauso(self):
        return self.mauso

    def Nghichdao(self):
        print(self.mauso,"/",self.tuso)

    def GT(self):
        return float(self.tuso/self.mauso)

    def Toigian(self):
        UCLN = math.gcd(self.tuso, self.mauso)
        print(int(self.tuso/UCLN),"/",int(self.mauso/UCLN))

    def SS(self, ps1):
        pass

    def Cong(self):
        pass

    def Tru(self):
        pass

    def Nhan(self):
        pass

    def Chia(self):
        pass

ps1 = Function(2, 3)
print("Nhập phân số 1:")
ps1.Nhap()
print("\nPhân số 1 có dạng:")
ps1.Xuat()

print('\nTử số ps1:', ps1.Tuso())
print('Mẫu số ps1:', ps1.Mauso())

print('\nNghịch đảo ps1:')
ps1.Nghichdao()
print('\nGiá trị ps1:', ps1.GT())
print('\nPs1 sau khi tối giản:')
ps1.Toigian()

ps2 = Function(5,1)
print("Nhập phân số 2:")
ps2.Nhap()
print("Phân số 2 có dạng:")
ps2.Xuat()

print('Tử số ps2:', ps2.Tuso())
print('Mẫu số ps2:', ps2.Mauso())

ps = ps1.GT() - ps2.GT()
if ps > 0:
    print("Ps1 lớn hơn Ps2")
elif ps < 0:
    print("Ps1 nhỏ hơn Ps2")
else:
    print("Ps1 bằng Ps2")