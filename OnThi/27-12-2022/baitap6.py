dem = {}
sdt = "0355733881"
for kytu in sdt:
    dem[kytu] = dem.get(kytu, 0)+1

sodienthoai = sorted(dem.keys())
for num in sodienthoai:
    print("%s:%d" %(num, dem[num]))
print()

chuoi = "chao anh ban nhe"
chuoi.strip()
chuoi = chuoi.replace(" ", "-")

dem1 = {}
for kytu in chuoi:
    dem1[kytu] = dem1.get(kytu, 0)+1

ketqua = sorted(dem1.keys())
for kytu in ketqua:
    print("%s:%d" %(kytu, dem1[kytu]))

dem2 = {}
chuoi_ae = ['chao', 'hi', 'chao', 'hello', 'blabla']
for tu in chuoi_ae:
    dem2[tu] = dem.get(tu, 0)+1
print()

ketqua2 = sorted(dem2.keys())
for tu in ketqua2:
    print("%s:%d" %(tu, dem2[tu]))
