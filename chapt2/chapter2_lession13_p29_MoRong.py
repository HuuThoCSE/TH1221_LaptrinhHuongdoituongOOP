# Chapter2_lession11_p29
RealMoney = float(input("Nhập vào số tiền thực của một tài khoản ngân hàng: "))

while True:
    print("\nBạn muốn: ")
    print("1. Gửi vào.")
    print("2. Rút ra. ")
    choose_type = int(input("Sự lựa chọn của bạn: "))
    if choose_type == 1:
        money = float(input("Nhập số tiền bạn muốn gửi vào: "))
        while money < 0:
            print("Số tiền gửi vào phải lớn hơn 0.")
            money = float(input("Nhập số tiền bạn muốn gửi vào: "))
        RealMoney = RealMoney + money
        print("Số tiền thực tại:", RealMoney)
    elif choose_type == 2:
        money = float(input("Nhập số tiền bạn muốn rút: "))
        while money < 0:
            print("Số tiền rút phải lớn hơn 0.")
            money = float(input("Nhập số tiền bạn muốn rút: "))
        while money > RealMoney:
            print("Số tiền rút phải nhỏ hơn số tiền thực.")
            money = float(input("Nhập số tiền bạn muốn rút: "))
        RealMoney = RealMoney - money
        print("Số tiền thực tại:", RealMoney)
    print("\nBạn có muốn muốn sử dụng thêm dịch vụ gì không")
    print("1. Có.")
    print("2. Không. ")
    choose_continue = int(input("Sự lựa chọn của bạn: "))
    if(choose_continue == 2):
        exit(0)