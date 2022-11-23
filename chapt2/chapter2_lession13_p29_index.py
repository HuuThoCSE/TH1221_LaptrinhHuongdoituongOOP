# Chapter2_lession13_p29
SoTienThuc = 0;
while True:
    NhatKy = input("Nhập nhật ký giao dịch (D/W <So tien>): \n")
    NhatKy = NhatKy.split(" ")
    Type = NhatKy[0]
    Money = int(NhatKy[1])

    if Money < 0:
        print("Số tiền nhỏ hơn 0.")
        print("=> ", SoTienThuc)
        break

    if Type == "D":
        SoTienThuc += int(Money)
        print("=> ", SoTienThuc)
    elif Type == "W":
        if(Money > SoTienThuc):
            print("Số tiền rút lớn hơn số tiền thực.")
        else:
            SoTienThuc -= int(Money)
            print("=> ", SoTienThuc)
    print("-----------------------------")