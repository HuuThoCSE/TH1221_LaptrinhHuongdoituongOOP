class clock:
    def __init__(self,g=0,p=0,gi=0):
        self.gio=g
        self.phut=p
        self.giay=gi

    def Nhap(self):
        self.gio = int(input("Nhập giờ: "))
        while(self.gio<0 or self.gio>23):
            self.gio = int(input("Nhập lại giờ: "))

        self.phut = int(input("Nhập phút: "))
        while(self.phut < 0 or self.phut > 59):
            self.phut = int(input("Nhập lại phút:"))

        self.giay = int(input("Nhập giây: "))
        while(self.giay<0 or self.giay>59):
            self.giay = int(input("Nhập lại giây: "))

    def Xuat(self):
        print("[",self.gio,"-",self.phut,"-",self.giay,"]")

    def __add__(self, Number):
        self.giay += Number
        while(self.giay>=60):
            self.phut += 1
            self.giay = 0 + self.giay-60
        while(self.phut>=60):
            self.gio += 1
            self.phut = 0 + self.phut-60
        return print("[",self.gio,"-",self.phut,"-",self.giay,"]")

    def __sub__(self, Number):
        self.giay -= Number
        while(self.giay<=0):
            self.phut -= 1
            self.giay = 60--self.giay
        while(self.phut<=0):
            self.gio -= 1
            self.phut = 60--self.phut
        return print("[",self.gio,"-",self.phut,"-",self.giay,"]")

    def __and__(self, clock2):
        if(self.gio > 12 and clock2.gio >12):
            return True
        else:
            return False

    def __or__(self, clock2):
        if(self.phut >= 30 or clock2.phut >=30):
            return True
        else:
            return False
    def __xor__(self, clock2):
        if(self.giay < 30 and clock2.giay >= 30 or self.giay >= 30 or clock2.giay <30):
            return True
        else:
            return False

    def __invert__(self):
        if(self.gio<12 and self.phut<30 and self.giay<30):
            return True
        else:
            return False

    def __lt__(self, clock2):
        time1 = self.gio * 24 * 60 + self.phut * 60 + self.giay
        time2 = clock2.gio * 24 * 60 + clock2.phut * 60 + clock2.giay
        if (time1 < time2):
            return True
        else:
            return False

    def __le__(self, clock2):
        time1 = self.gio * 24 * 60 + self.phut * 60 + self.giay
        time2 = clock2.gio * 24 * 60 + clock2.phut * 60 + clock2.giay
        if (time1 <= time2):
            return True
        else:
            return False

    def __gt__(self, clock2):
        time1 = self.gio * 24 * 60 + self.phut * 60 + self.giay
        time2 = clock2.gio * 24 * 60 + clock2.phut * 60 + clock2.giay
        if (time1 > time2):
            return True
        else:
            return False

    def __ge__(self, clock2):
        time1 = self.gio * 24 * 60 + self.phut * 60 + self.giay
        time2 = clock2.gio * 24 * 60 + clock2.phut * 60 + clock2.giay
        if (time1 <= time2):
            return True
        else:
            return False

    def __eq__(self, clock2):
        time1 = self.gio * 24 * 60 + self.phut * 60 + self.giay
        time2 = clock2.gio * 24 * 60 + clock2.phut * 60 + clock2.giay
        if (time1 == time2):
            return True
        else:
            return False

    def __ne__(self, clock2):
        time1 = self.gio * 24 * 60 + self.phut * 60 + self.giay
        time2 = clock2.gio * 24 * 60 + clock2.phut * 60 + clock2.giay
        if (time1 != time2):
            return True
        else:
            return False

Time1 = clock(16, 59, 59)
Time1.Xuat()

Time1.__add__(12)

Time2 = clock(15, 0, 00)
Time2.__sub__(12)

if(Time1.__and__(Time2)):
    print("Cả 2 clock đều có số giờ lớn hơn 12")
else:
    print("Cả 2 clock đều không có số giờ lớn hơn 12")

if(Time1.__or__(Time2)):
    print("Cả 2 clock có ít nhất 1 trong 2 clock có số phút lớn hơn bằng 30")
else:
    print("Cả 2 clock không có ít nhất 1 trong 2 clock có số phút lớn hơn bằng 30")

if(Time1.__xor__(Time2)):
    print("Chỉ có một 1 clock có số giây lớn hơn 30")
else:
    print("Không có một 1 clock nào có số giây lớn hơn 30")

if(Time1.__invert__()):
    print("Clock có số giờ nhỏ hơn 12 và số phút nhỏ hơn 30 và số giây nhỏ hơn 30")
else:
    print("Clock không có số giờ nhỏ hơn 12 và số phút nhỏ hơn 30 và số giây nhỏ hơn 30")

if(Time1.__lt__(Time2)):
    print("Clock1 nhỏ hơn Clock2")
else:
    print("Clock1 không nhỏ hơn Clock2")

if(Time1.__le__(Time2)):
    print("Clock1 nhỏ hơn bằng Clock2")
else:
    print("Clock1 không nhỏ hơn bằng Clock2")

if(Time1.__gt__(Time2)):
    print("Clock1 lớn hơn Clock2")
else:
    print("Clock1 không nhỏ hơn Clock2")

if(Time1.__eq__(Time2)):
    print("Clock1 bằng Clock2")
else:
    print("Clock1 không bằng Clock2")

if(Time1.__ne__(Time2)):
    print("Clock1 không bằng Clock2")
else:
    print("Clock1 bằng Clock2")