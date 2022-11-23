# str="Anhrat123@"
str=input("Nhập Password: ")
Status_ChuCai_Thuong=False
Status_ChuSo=False
Status_ChuCai_Hoa=False
Status_KyTuDacBiet=False
Status_DoDaiToiThieu=False
Status_DoDaiToiDa=False
for kt in str:
    if kt.islower():
        Status_ChuCai_Thuong = True

    if kt.isdigit():
        Status_ChuSo = True

    if kt.isupper():
        Status_ChuCai_Hoa = True

    if kt.isalnum():
        Status_KyTuDacBiet = True

if len(str) >= 6:
    Status_DoDaiToiThieu = True

if len(str) <= 12:
    Status_DoDaiToiDa = True

if(Status_ChuCai_Thuong and Status_ChuSo and Status_ChuCai_Hoa and Status_KyTuDacBiet and Status_DoDaiToiThieu and Status_DoDaiToiDa):
    print("Mật khẩu hợp lệ.")
else:
    print("Mật khẩu không hợp lệ.")