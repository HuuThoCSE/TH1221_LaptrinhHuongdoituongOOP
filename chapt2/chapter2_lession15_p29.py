# Chapter2_lession11_p29

n = int(input("Nhập vào số nguyên dương n="))
S = 0
for i in range(1, n+1):
    S += i / (i + 1)
    print(S, "\t", i)

# # Chay theo mẫu
# for i in range(1, n+1):
#     S += (i-1)/i
#     print(S, "\t", i)

print("Tổng S=", S)