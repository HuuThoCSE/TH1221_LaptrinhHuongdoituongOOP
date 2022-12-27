thuc = 0
while True:
    print("Nhập nhật ký: ")
    query = input()
    query = query.split(" ")

    if query[0] == "D":
        if (int(query[1]) < 0):
            print("Số tiền gửi hoặc rút phải là số dương.")
        else:
            thuc += int(query[1])

    elif query[0] == "W":
        if (int(query[1]) > thuc):
            print("Số tiền rút không thể lớn hơn số tiền gửi hiện tại")
        else:
            thuc -= int(query[1])
    print("Số tiền thực:", thuc)