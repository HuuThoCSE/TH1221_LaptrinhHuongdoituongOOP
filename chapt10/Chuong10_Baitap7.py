filename = input("Nhập vào tên file: ")

# Đếm dòng
f = open(filename, 'r', encoding='utf-8')
with f as f:
    size = len([0 for _ in f])
f.close()

print(f'File co {size}')