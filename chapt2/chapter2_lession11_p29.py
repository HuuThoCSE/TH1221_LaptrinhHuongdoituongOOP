# Chapter2_lession11
s = 1;
number = float(input("Nhập số thực: "))
while number != 0:
    if number > 0:
        s = s * number
    number = float(input("Nhập số thực: "))
print("Giá trị tính tích các số thực đã nhập:", s)
