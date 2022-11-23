try:
    BieuThuc = input("Nhập vào 1 biểu thức: ")
    kq = eval(BieuThuc)
    print(BieuThuc, '=', kq)
except (ValueError, SyntaxError, NameError):
    print('Biểu thức không hợp lệ.')