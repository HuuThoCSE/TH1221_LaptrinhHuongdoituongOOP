# num = int(input("Nhập số nguyên có 4 chữ số: "))
num = 3125
sum_num =0

ChuSoCuoi = num % 10
sum_num +=ChuSoCuoi # 5

num /= 10
ChuSo3 = num % 10
sum_num +=ChuSo3 # 2
print(ChuSo3)

num /= 10
num %= 10
ChuSo2 = num % 10
sum_num +=ChuSo2 # 1

num /= 10
num %= 10
ChuSoDau = num % 10
sum_num +=ChuSoDau # 3

print(sum_num)
print(ChuSoDau)
print(ChuSoCuoi)