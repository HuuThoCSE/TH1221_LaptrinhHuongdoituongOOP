from datetime import date
class Nguoi():
    def __init__(self, ht: str):
        self.ht = ht

class ThanhVien(Nguoi):
    def __init__(self, ht: str, ns: int):
        super(ThanhVien, self).__init__(ht)
        self.ns = ns

    def Xuat(self):
        print("Họ tên:", self.ht)
        print("Năm sinh:", self.ns)

ds = [ThanhVien("Nguyen Huu Tho", 2003),
      ThanhVien("Nguyen Van Hoang", 2002),
      ThanhVien("Le Nguyen Quan Binh", 2001),
        ThanhVien("Nguyen Thanh Tam", 2000)
      ]

import operator
ds.sort(key=operator.attrgetter("ns"), reverse=False)
print(ds)

n = len(ds)
for i in range(0, n):
    ds[i].Xuat()