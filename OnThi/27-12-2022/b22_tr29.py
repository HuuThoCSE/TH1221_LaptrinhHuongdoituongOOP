def Fibonacci(n):Fibonacci(n)
    if n<0:
        return -1
    if n==0 or n==1:
        return n
    return Fibonacci(n-1)+Fibonacci(n-2)

n = 30
for i in range(1, n+1):
    print(Fibonacci(n))