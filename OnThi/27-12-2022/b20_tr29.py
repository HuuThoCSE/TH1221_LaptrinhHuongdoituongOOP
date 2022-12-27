N = 30
print("In cac so nguyen to: ", end="")
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
    # if(i==2):
    #     print(i, end=' ')
    # for j in range(2, int(i**0.5)+1):
    #     if i%j!=0:
    #         print(i, end=" ")
    if SNT(i)==True:
        print(i, end=', ')