# 6. Viết chương trình nhập vào bán kính của hình tròn, in ra diện tích, chu vi của nó.
import math
r = float(input("Nhập vào bán kinh hình tròn: "))
pi = math.pi
dt = 2*pi*r**2
cv =  2*pi*r
print("Diện tích hình tròn:", format(dt, '.6f')) # Hiện [số lượng] chữ số lẽ
print("Chu vi hình tròn:", format(cv, '.6f'))