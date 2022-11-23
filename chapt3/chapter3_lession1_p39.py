# Chapter3_lession1_p39
st=input("Nhập vào chuỗi bất kỳ: ")
Dem_KT_DacBiet=0
Dem_ST=0
for kt in st:
    if kt.isalnum():
        Dem_KT_DacBiet+=1
print("Số ký tự đặc biệt là:", Dem_KT_DacBiet)

for i in st:
    if(i!=''):
        Dem_ST +=1
print("Trong chuỗi có", Dem_ST, "từ")