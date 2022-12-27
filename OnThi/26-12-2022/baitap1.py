l = []
n = 5
import random
for i in range(n):
    l.append(random.randrange(0, 100))

for i in range(n):
    print(l[i])

k = 2
print(f"DS uoc so cua {k}: ", end="")
for i in range(n):
    if i%k == 0:
        print(i, end=" ")
print("\nPhần tử lớn nhất trong DS:", max(l))

