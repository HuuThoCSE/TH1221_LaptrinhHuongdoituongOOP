class Fraction:
    '''Lớp Fraction gồm 2 thuộc tính, 4 phương thức
    và 3 hàm quá tải'''
    def __init__(self, tu = 0, mau = 1):
        self.ts = tu
        self.ms = mau

    def Nhap(self):
        tu = int(input("Nhập tử số:"))
        self.ts = tu
        mau = int(input("Nhập mẫu số:"))
        while mau == 0:
            mau = int(input("Nhập mẫu số:"))
        self.ms = mau

    def Xuat(self):
        if self.ts == 0:
            print(0)
        elif self.ms == 1:
            print(self.ts)
        elif self.ts < 0 and self.ms < 0:
            print(abs(self.ts), '/', abs(self.ms))
        elif self.ts > 0 and self.ms < 0:
            print(-self.ts, '/', abs(self.ms))
        else:
            print(self.ts, '/', self.ms)

    def Toigian(self):
        if self.ts < self.ms:
            i = self.ts
        else:
            i = self.ms

        while self.ts % i != 0 or self.ms % i != 0:
            i -= 1
        tu = self.ts // i
        mau = self.ms // i
        return Fraction(tu, mau)

    def __gt__(self, ob2):
        tu1 = self.ts * ob2.ms
        tu2 = ob2.ts * self.ms
        if tu1 > tu2:
            return True
        else:
            return False
    def __le__(self, ob2):
        tu1 = self.ts * ob2.ms
        tu2 = ob2.ts * self.ms
        if tu1 <= tu2:
            return True
        else:
            return False
    def __eq__(self, ob2):
        tu1 = self.ts * ob2.ms
        tu2 = ob2.ts * self.ms
        if tu1 == tu2:
            return True
        else:
            return False
ps1 = Fraction()
ps1.Nhap()
ps1.Xuat()

pstg = ps1.Toigian()
pstg.Xuat()

ps2 = Fraction()
ps2.Nhap()
ps2.Xuat()

if ps1 > ps2:
    print('Phân số 1 lớn hơn phân số 2')
else:
    print('Phân số 1 KHÔNG lớn hơn phân số 2')
if ps1 <= ps2:
    print('Phân số 1 nhỏ hơn hoặc bằng hơn phân số 2')
else:
    print('Phân số 1 KHÔNG nhỏ hơn hoặc bằng phân số 2')
if ps1 == ps2:
    print('Phân số 1 bằng với phân số 2')
else:
    print('Phân số 1 KHÔNG bằng phân số 2')
