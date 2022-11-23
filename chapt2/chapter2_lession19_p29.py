number = float(input("Nhập vào lần lượt các số thực: "))
count = 0
s = 0
while number != 0 :
    count += 1
    s = s + number
    number = float(input())
print("s=", s/count)