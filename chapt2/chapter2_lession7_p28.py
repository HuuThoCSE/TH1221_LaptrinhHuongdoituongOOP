# 7. Viết chương trình đếm số ước số của một
# số nguyên dương được nhập vào từ bàn phím.

n = int(input("Nhập vào một số nguyên: "))
dem = 0
for i in range(1, n+1):
  if(n % i == 0):
    dem += 1
print("Số ước số của",n,"là", dem)
print(n, "Có", dem , "uocs số.")