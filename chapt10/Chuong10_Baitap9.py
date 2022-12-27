# Cach1
f = open('Lthdt.txt', 'r', encoding='utf-8')
nd = f.read()

f2 = open('Lthdt - Copy.txt', 'w', encoding='utf-8')
f2.write(nd)
f2.close()
f.close()

# Cach2
f = open('Lthdt.txt', 'r', encoding='utf-8')
with f as f:
    size = len([0 for _ in f])
f.close()

f = open('Lthdt.txt', 'r', encoding='utf-8')
f2 = open('Lthdt - Copy2.txt', 'w', encoding='utf-8')
for i in range(0, size):
    nd = f.readline()
    f2.write(nd)
f2.close()
f.close()

# Cach3
import shutil
shutil.copy('Lthdt.txt', 'Lthdt - Copy3.txt')
