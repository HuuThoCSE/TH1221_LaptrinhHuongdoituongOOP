bieuthuc = print("Nhập biểu thức: ")
try:
    kq = eval(bieuthuc)
    print(bieuthuc,"=",kq)
except(ValueError, NameError, SyntaxError):
    print("Biểu thức không hợp lệ.")