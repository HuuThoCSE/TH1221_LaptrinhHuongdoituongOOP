import random
# a = int(input("Nhập số nguyên dương a: "))
# b = int(input('Nhập số nguyên dương b lớn hơn a: '))
# while a >= b:
#     b = int(input('Nhập số nguyên dương b lớn hơn a: '))

a = 5
b = 100

list1 = random.sample(range(a, b+1), 5)
print("Danh sach list1 la", list1)
# Cach khac: Cho biet su khac hau giua 2 cach???
# list1 = []
# for i in range(5):
#     so = random.randint(a, b)
#     list1.append(so)
# print("Danh sach list 1 la: ", list)

list2 = random.sample([i for i in range(a, b+1) if i%2!=0], 10)
print("Danh sach list2 la: ", list2)

k = int(input("Nhap so PhTu can tao: "))
list3 = random.sample([i for i in range(a, b+1) if i%5==0 and i%7==0], k)
print('Danh sach list3 la: ', list3)
random.shuffle(list3) # random.shuffle Tron DS lại

list4 = list3
print("Danh sach list4 la:", list4)