# 5. Viết chương trình tính giai thừa của một số nguyên dương được nhập vào từ bàn phím.

songuyenduong = int(input("Nhập vào một số nguyên dương: "))
kq = 1
for i in range(1, songuyenduong+1):
  kq *= i
  print(i, sep='*')
print("Kết quả:", kq)