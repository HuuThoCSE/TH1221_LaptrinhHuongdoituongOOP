D = input("Nhập vào 3 số (Vd: 18, 22, 24): ")
D = D.split(",")
C = 50
H = 30
for i in D:
    Q = int((((2*C*int(i))/H)**(1/2)))
    print(",".join(Q))