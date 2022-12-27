N = 50
def SNT(n):
    if n<2:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3, n, 2):
            if n%i==0:
                return False
            else:
                return True
for i in range(1, N+1):
    if SNT(i):
        print(i, end=" ")