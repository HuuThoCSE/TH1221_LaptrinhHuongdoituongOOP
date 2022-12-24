# đếm chữ có thể số chuyển hoa ...
def dem(n):
    d = 0
    for i in n:
        if i.isalpha() == True:
            d = d + 1
    return d


# in từng từ và đếm từ
def intu(n):
    a = n.split(" ")
    dem = 0
    for i in a:
        if i != ' ':
            dem = dem + 1
            print(i)
    print("Co ", dem, " tu")


# xóa khoảng trắng dư thừa
def xoa(n):
    n = n.strip()
    i = 1
    while i < len(n) - 1:
        if n[i] == ' ' and n[i + 1] == ' ':
            n = n[:i] + n[i+1:]
        else:
            i=i+1
    return n

#in họ và tên
def hoten(n):
    a=n.find(' ')
    ho=n[:a]
    b=n.rfind(' ')
    ten=n[b+1:]
    print("HO: ", ho, " TEN: ", ten)

#in từ xuất hiện nhiều nhất
def max(n):
    max={}
    #split tách ra thành từng từ nếu không tách sẽ là  từng chữ
    a = n.split(" ")
    for i in a:
        if i in max:
            max[i]+= 1
        else:
            max[i] = 1
    m=0
    for i in sorted(max, key=max.get, reverse=False):
        if max[i]>m:
            m = max[i]
            mx =  i
    print("Tu xuat nhien nhat la: ", mx, " so lan la: ", m)


###
n = input("Nhap vao chuoi bat ky: ")
print("Co ", dem(n), " ki tu chu")
print(intu(n))
print(xoa(n))
print(hoten(n))
print(max(n))