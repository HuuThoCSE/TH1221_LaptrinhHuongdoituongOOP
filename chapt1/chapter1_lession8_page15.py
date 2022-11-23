# 8. Viết chương trình nhập vào 1 số phức, cho biết mô đun và số phức liên hợp của số phức đã nhập.

real = int(input("Nhập vào Phần thực: "))
imag = int(input("Nhập vào Phần ảo: "))
print("Phần thực: ", real)
print("Phần ảo: ", imag)

z = complex(real, imag)
print("Mô đun số phức:", abs(pow(((real**2)+(imag**2)), 1/2)))
z2 = complex(real, -imag)
print("Số phức liên hơp:", z2)