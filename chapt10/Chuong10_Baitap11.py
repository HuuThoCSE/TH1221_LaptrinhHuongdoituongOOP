import random
filename = input("Nhập vào tên file: ")

# Đếm dòng
f = open(filename, 'r', encoding='utf-8')
with f as f:
    size = len([0 for _ in f])
f.close()

num_line = random.randrange(0, size)
f = open(filename, 'r', encoding='utf-8')
for i in range(0, size):
    nd = f.readline()
    if(i == num_line):
        print(nd)
