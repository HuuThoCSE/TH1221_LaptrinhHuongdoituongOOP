import string
import re
me= '(\w+)@(\w+).(com)'

m=input("Nhập 1 chuỗi bất kì: ")
kq= re.match(me,m)
print("username là: ",kq.group(1))
print("Companyname là: ", kq.group(2))

