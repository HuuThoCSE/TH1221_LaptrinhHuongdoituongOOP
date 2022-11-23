#import sys
# epsilon = sys.float_info.epsilon

while True:
    epsilon = float(input("Nhập vào 1 lượng epsilon nhỏ hơn 1: "))
    if epsilon < 1:
        break

e = 1
i = 1
gt = 1
sh = 1/gt
while sh >= epsilon:
    e += sh
    i += 1
    sh = 1/gt

print("Tổng e=", e)