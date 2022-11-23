# 14. Viết chương trình nhập vào năm sinh của 1 người. Cho biết người đó năm nay được bao nhiêu tuổi.

# Cách 2
from datetime import date # date -> today | now -> !=
birthday = int(input("Nhập vào năm sinh: "))
old = date.today().year-birthday
print("Năm nay bạn được",old,"tuổi.")