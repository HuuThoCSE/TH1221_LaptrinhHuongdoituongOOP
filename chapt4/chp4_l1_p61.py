# list_int = [1,2,3,5,6,6]
# n = 5

# list_int = []
# n = int(input("Nhập số lượng phần tử: "))

# Data test
list_int = []
n = 5
import random
for i in range(0, n):
    list_int.append(random.randrange(1, 100))

# for i in range(0, n):
#     x = int(input("Nhập vào một số nguyên: "))
#     list_int.append(x)

# In list
print(list_int)

print("\nLọc ra chữ số lẻ: ")
list_SoLe = [x for x in list_int if x%2!=0]

print(list_SoLe)

print("\nLoại bỏ các phần tử trùng: ")
list_SoLe = list(set(list_SoLe))
print(list_SoLe)