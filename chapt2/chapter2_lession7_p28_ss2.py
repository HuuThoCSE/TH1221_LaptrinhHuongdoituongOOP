# 7. Viết chương trình đếm số ước số của một
# số nguyên dương được nhập vào từ bàn phím.

#Cach 2 | Chỉ có bài này 2 là đúng
n = int(input("Nhập vào một số nguyên: "))
dem = 2
for i in range(2, n):
  if(n % i == 0):
    dem += 1
print("Số ước số của",n,"là", dem)
print(n, "Có", dem , "ước số.")