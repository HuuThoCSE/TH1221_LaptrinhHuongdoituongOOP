def Fibo(n):
    if n < 1:
        return n
    elif n==1 or n==2:
        return 1
    else:
        return Fibo(n-1)+Fibo(n-2)

n = 30
for i in range(n+1):
    print(i, end=" ")