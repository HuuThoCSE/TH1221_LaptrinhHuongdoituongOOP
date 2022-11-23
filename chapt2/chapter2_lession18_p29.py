# import sys
epsilon = sys.float_info.epsilon

while True:
    epsilon = float(input("Nhập vào 1 lượng epsilon nhỏ hơn 1: "))
    if epsilon < 1:
        break;
i = 1
e = 1
giaithua = 1

while epsilon <= 1.0/giaithua:
    giaithua *= i
    e = e+ 1.0/giaithua
    i += 1
print("e=", e)