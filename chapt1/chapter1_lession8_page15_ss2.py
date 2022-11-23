# 8. Viết chương trình nhập vào 1 số phức, cho biết mô đun và số phức liên hợp của số phức đã nhập.
z = complex(input("Nhập vào một số phức: "))
real = int(z.real)
imag = int(z.imag)
print("Phần thực: ", real)
print("Phần ảo: ", imag)
print("Mô đun số phức:", abs(pow(((real**2)+(imag**2)), 1/2)))
imag2 = -imag
z2 = complex(real, imag2)
print("Số phức liên hơp:", z2)