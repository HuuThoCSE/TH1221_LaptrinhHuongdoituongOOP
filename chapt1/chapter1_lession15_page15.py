# 15. Viết chương trình tạo ra các số thập phân ngẫu nhiên bằng cách sử dụng module
# random và các hàm random() và randrange():
# - Có giá trị nằm trong khoảng từ 0 đến 1.
# - Có giá trị nằm trong khoảng từ 10 đến 100.
# - Có giá trị nằm trong khoảng từ 7 đến 97.
# - Có giá trị nằm trong khoảng từ 9 đến 18.

import random
print("Có giá trị nằm trong khoảng từ 0 đến 1:", format(random.random(), ".3f"))
print("Có giá trị nằm trong khoảng từ 10 đến 100:", format(random.uniform(10,100), ".3f"))
print("Có giá trị nằm trong khoảng từ 10 đến 100:", format(random.uniform(7,97), ".3f"))
print("Có giá trị nằm trong khoảng từ 9 đến 18:", format(random.uniform(9,18), ".3f"))