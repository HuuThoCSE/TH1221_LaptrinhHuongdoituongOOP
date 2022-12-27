filename = input("Nhập vào tên file: ")
n = int(input("Nhập vào số dòng cần hiện: "))

# Đếm dòng
f = open(filename, 'r', encoding='utf-8')
with f as f:
    size = len([0 for _ in f])
# f.close()

# In dòng
f = open(filename, 'r', encoding='utf-8')
for i in range(0, size):
    nd = f.readline()
    if(i >= size-n):
        print(nd, end='')
f.close()