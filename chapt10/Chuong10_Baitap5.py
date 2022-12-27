filename = input("Nhập vào tên file: ")

f = open(filename, 'r', encoding='utf-8')
nd = f.read()
f.close()

tuDaiNhat = ""
dsCacTu = nd.split()
print(dsCacTu)
for tu in dsCacTu:
    if (len(tu) > len(tuDaiNhat)) or (len(tu) == len(tuDaiNhat) and tu < tuDaiNhat):
        tuDaiNhat = tu

print("Từ dài nhất:", tuDaiNhat)