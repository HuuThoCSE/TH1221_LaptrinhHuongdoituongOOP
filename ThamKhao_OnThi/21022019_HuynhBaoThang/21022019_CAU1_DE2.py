# 21022019_Huynh Bao Thang_CAU2_DE2_16
n = int((input("Nhập vào số nguyên dương n:")))
if n == 10:
    print("Dữ liệu không hợp lệ")
while n%2!=0 or n>=10:
    n = int((input("Nhập vào số nguyên dương n:")))

for i in range(1,n+1):
    print("*"*i)