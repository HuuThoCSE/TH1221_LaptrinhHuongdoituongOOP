class Phone:
    def __init__(self):
        self.brand = 'Nokia'
        self.version = '105 Single'
        self.price = 370
        self.ram = 4
        self.screen = 1.77
        self.pin = 800
        self.sim = 1
    def use(self):
        print('call, listen, save number, message')

    def sell(self):
        print('Thế giới di động, Điện máy xanh, Cửa hàng điện thoại.')

class Camera:
    def __init__(self):
        self.brand = 'Samsung'
        self.version = 'Ultra'
        self.price = 2500
        self.megapixel = 108
        self.size = 1.33
        self.aperture = 'F/1.8'

    def use(self):
        print('take photograph, record')

    def sell(self):
        print('Thế giới di động, Điện máy xanh, Cửa hàng điện tử')

class SmartPhone(Phone, Camera):
    def __init__(self):
        Phone.__init__(self)
        Camera.__init__(self)
    def info_in(self):
        self.price = float(input("Nhập giá: "))
        self.screen = float(input("Nhập kích thước màn hình: "))
        self.sim = int(input("Nhập số sim: "))
        self.megapixel = float(input("Nhập độ phân giải: "))

    def info_out(self):
        print("Thông tin về Smartphone: ")
        print("Brand: ", self.brand)
        print("Version: ", self.version)
        print("Price: ", self.price)
        print("Ram: ", self.ram)
        print("Screen", self.screen)
        print("Pin: ", self.pin)
        print("Sim: ", self.sim)
        print("Megapixel: ", self.megapixel)
        print("Size", self.size)
        print("Aperture: ", self.aperture)

    def use_sm(self):
        print("Chức năng chính của Smartphone: ")
        Phone.use(self)
        Camera.use(self)
        print('internet, game, ...')

    def sell_sm(self):
        print("Smartphone bán tại: ")
        Phone.sell(self)
        print("Cửa hàng điện tử, siêu thị, ...")

sm = SmartPhone()
sm.info_in()
sm.info_out()
sm.use_sm()
sm.sell_sm()
