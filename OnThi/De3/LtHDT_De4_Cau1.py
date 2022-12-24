def Fibonacci_DQ(n):
    if n <= 1:
        return n
    return Fibonacci_DQ(n-1)+Fibonacci_DQ(n-2)

for i in range(10):
    print(Fibonacci_DQ(i), end=' ')
print()

def Fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

for i in range(10):
    print(Fibonacci(i), end=' ')