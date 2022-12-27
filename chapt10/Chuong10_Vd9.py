f2 = open('Lthdt.txt', 'r', encoding='utf-8')
print(f2.tell())

nd = f2.readline()
print(f2.tell())

f2.seek(0, 1)
print(f2.tell())

f2.seek(0, 0)
print(f2.tell())

f2.seek(0, 2)
print(f2.tell())