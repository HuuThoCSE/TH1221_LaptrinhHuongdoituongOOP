class clock:
    def __init__(self,g='gio',p='phut',gi='giay'):
        self.gio=g
        self.phut=p
        self.giay=gi
    def nhap(self):
        self.gio = int(input("Nhap gio: "))
        while(self.gio<0 or self.gio>23):
            print("nhap lai gio")
            self.gio = int(input("Nhap gio: "))
        self.phut = int(input("Nhap phut: "))
        while(self.phut < 0 or self.phut > 59):
            print("nhap lai phut")
            self.phut = int(input("Nhap phut: "))
        self.giay = int(input("Nhap giay: "))
        while(self.giay<0 or self.giay>59):
            print("nhap lai giay")
            self.giay = int(input("Nhap giay: "))
    def xuat(self):
        print("so gio hien tai la:",self.gio,":",self.phut,":",self.giay)

    def XuatCong(self):
        if (self.giay == 59):
            self.phut = self.phut + 1
        elif (self.phut == 59):
            self.gio = self.gio + 1
        print("so gio phut giay sao khi cong:", self.gio, ":", self.phut, ":", self.giay)

    def XuatTru(self):
        if (self.giay == 59):
            self.phut = self.phut - 1
            self.giay = self.giay + 1
        elif (self.phut == 59):
            self.gio = self.gio - 1
        print("so gio phut giay sao khi tru:", self.gio, ":", self.phut, ":", self.giay)

A = clock()
A.nhap()
A.xuat()
A.XuatCong()
A.XuatTru()