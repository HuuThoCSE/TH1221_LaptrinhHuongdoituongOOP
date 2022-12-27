filename = input("Nhập vào tên file: ")
n = int(input("Nhập vào số dòng cần hiện: "))

with open(filename, 'r', encoding='utf-8') as f:
    last_line = f.readlines()[-1]+'\n'

print(last_line*n)
f.close()