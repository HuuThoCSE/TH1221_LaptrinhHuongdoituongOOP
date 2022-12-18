# Nếu số nào mà N chia hết cho nó thì nó là ước só
N = int(input("Nhập vào số nguyên dương: "))

while N < 10 or N > 99:
    N = int(input("Nhập lại số nguyên dương: "))

print("Ước số lẻ theo thứ tự tăng dần: ")
for i in range (1, N+1):
   if N%i == 0 and i%2!=0:
       print(i, end='\t')

# !!!