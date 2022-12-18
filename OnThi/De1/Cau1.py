CT = int(input("Nhập vào giá trị Cycle Threhold: "))
while CT < 10 or CT > 45:
    CT = int(input("Nhập lại giá trị Cycle Threhold: "))

if CT > 40:
    print("Âm tính.")
elif CT > 33:
    print("Không lây nhiễm")
elif CT >= 30:
    print("Cách ly tại nhà")
elif CT < 30:
    print("Cách ly tập trung")