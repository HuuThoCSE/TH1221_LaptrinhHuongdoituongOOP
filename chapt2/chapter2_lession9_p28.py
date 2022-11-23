# 9. Viết chương trình tính và in giá trị của Q cho bởi công thức: Q = √(2 ∗ C ∗ D)/H .
# Với giá trị cố định của C là 50, H là 30, D là dãy các giá trị được nhập từ bàn phím
# với các giá trị của D được phân cách bằng dấu phẩy. Giả sử dãy giá trị của D nhập vào
# là 100,150,180 thì các giá trị của Q sẽ là 18,22,24.

C = 50
H = 30
D = input("Nhập dãy các giá trị được phân cách bởi dấu phẩy: ")
D = D.split(",")
print("Kết quả:")
for i in D:
  Q = int(((2*C*int(i)/H))**(1/2))
  print(Q, end=",")