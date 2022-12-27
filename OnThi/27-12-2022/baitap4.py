
n = 8

# for i in range(1, n+1):
#     for x in range(n-i):
#         print(end=" ")
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()
# print()
#
# for i in range(0, n):
#     for x in range(0, i):
#         print(end=" ")
#     for j in range(1, n+1-i):
#         print("*", end=" ")
#     print()
# print()
#
# for i in range(1, n+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()
# print()
#
# for i in range(n):
#     for j in range(n-i):
#         print("*", end=" ")
#     print()
#
# for i in range(1, n+1):
#     for x in range(1, n+1-i):
#         print(" ", end=" ")
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()
# print()
#
# for i in range(1, n+1):
#     for x in range(1, i):
#         print(" ", end=" ")
#     for j in range(1, n+2-i):
#         print("*", end=" ")
#     print()

# for i in range(n+1):
#     for j in range(n+1):
#         print("*", end=" ")
#     print()

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i==n or j==n or i==1 or j==1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# Tam giac Floyd
k = 1
n = 6
for i in range(1, n+1):
    for j in range(1, i+1):
        print("{:<2}".format(k), end=" ")
        k += 1
    print()