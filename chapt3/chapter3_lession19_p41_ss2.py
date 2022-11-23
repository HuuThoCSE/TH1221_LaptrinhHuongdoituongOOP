str="Nguyen%Huu$Tho12324444334"
# str=input("Nhập vào chuỗi bất kỳ: ")

Dem_KhongLa_ChuCai=0

for i in range(1, len(str)-1):
    if(str[i].isalpha() == False):
        Dem_KhongLa_ChuCai+=1

    if(str[i].isalpha() == True):
        str = str.upper()

print("Có", Dem_KhongLa_ChuCai, "ký tự không là chữ cái.")
print("Dang chuan UPPER:", str)

# Chu so xuat hien nhieu nhat
count={}
for i in str:
    if(i.isnumeric()):
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

# print(count)
max = 0
for i in sorted(count, key=count.get, reverse=False):
    if count[i] > max:
        max = count[i]
        max_value = i

print("Chữ số xuất hiện nhiều nhất", max_value, "với số lần xuất hiện là", max)
