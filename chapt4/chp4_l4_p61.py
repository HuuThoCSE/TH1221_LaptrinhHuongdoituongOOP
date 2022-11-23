import math
ds = []
# n = int(input("Nhập số lần di chuyển: "))
n = 4
# for i in range(0, n):
#     print("Nhap lan di thu", i+1, end=': ')
#     s = input()
#     ds.append(s)
ds = ['UP 5', 'DOWN 3', "LEFT 3", "RIGHT 2"]
x, y = 0,0
for i in ds:
    landc = i.split(" ")
    huong = landc[0]
    sobuocdi = int(landc[1])
    if huong == "UP":
        y += sobuocdi
    elif huong == "DOWN":
        y -= sobuocdi
    elif huong == "LEFT":
        x -= sobuocdi
    elif huong == "RIGHT":
        x =+ sobuocdi
    else:
        pass
kc = math.sqrt(x**2 + y**2)
print('Khoang cach tu tam den vi tri la', kc)