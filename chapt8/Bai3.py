from datetime import date
class Animal():
    def __init__(self,cn="",tt=100,sc=4,nss="",tk=""):
        self.cannang=cn
        self.tuoitho=tt
        self.sochan=sc
        self.noisinhsong=nss
        self.tiengkeu=tk
    def nhap(self):
        print("Nhap thong tin Animail")
        self.cannang=int(input("nhap so can nang:"))
        self.tuoitho=int(input("nhap tuoi tho cua chung:"))
        self.sochan=int(input("nhap so chan cua chung:"))
        self.noisinhsong=input("nhap noi sinh song :")
        self.tiengkeu=input("nhap tieng keu:")
    def xuat(self):
        print("so can nang cua chung la:",self.cannang)
        print("so tuoi tho cua chung la:", self.tuoitho)
        print("so chan cua chung la:", self.sochan)
        print("noi sinh song cua chug la vung:", self.noisinhsong)
        print("tieng keu cua chung la:", self.tiengkeu)
thu1=Animal()
thu1.nhap()
thu1.xuat()
class Predator(Animal):
    '''Predator ke thua Animal'''
    def __init__(self,cn="",tt=100,sc=4,nss="",tk="",tdc=""):
        self.tocdochay=tdc
        super().__init__(tt,sc,nss,tk,cn)
    def NhapPre(self):
        print("Nhap thong tin Predator")
        self.nhap()
        self.tocdochay = input("Nhap toc do chay: ")
    def XuatPre(self):
        print("Thong tin cua Predator")
        self.xuat()
        print("Toc do chay : ",self.tocdochay)

thu2=Predator()
thu2.NhapPre()
thu2.XuatPre()


class Lion(Predator):
    '''Lion ke thuc Predator'''
    def __init__(self,cn="",tt=100,sc=4,nss="",tk="",tdc="",cb=""):
        self.cobom=cb
        Predator.__init__(tt,sc,nss,tk,cn,tdc)
    def NhapLion(self):
        print("Nhap thong tin Lion")
        self.NhapPre()
        self.tocdochay = input("Co bom hay khong: ")
    def XuatLion(self):
        print("Thong tin Lion")
        self.xuatPre()
        print(self.tocdochay)

thu3=Lion()
thu3.NhapLion()
thu3.XuatLion()



