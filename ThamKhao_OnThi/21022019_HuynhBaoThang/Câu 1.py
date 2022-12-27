N = int(input("Nhập N:"))
if N == 10:
    print("Dữ liệu không hợp lệ")
while N%2 !=0 or N>=10:
    N = int(input("Nhập N:"))
for i in range(1,N+1):
    print((N-i)*" ",i*"* ")