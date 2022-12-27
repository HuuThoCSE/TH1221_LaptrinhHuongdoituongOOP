n=int(input("Nhập số nguyên dương chẵn N bé hơn 10: "))
if n%2==0 and n<10 and n>0:
    for i in range(1,n+1):
        for x in range(n-i):
            print(end=" ")
        for j in range(1,i+1):
            print("*",end=" ")
        print()
else: print("Dữ liệu ko hợp lệ!")