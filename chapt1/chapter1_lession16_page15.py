# 16. Viết chương trình nhập vào cân nặng (ký lô gam) và chiều cao (mét) của
# 1 người trưởng thành, tính chỉ số BMI và dự báo độ béo phì cho người này
# theo công thức và bảng sau:

can_nang = float(input("Nhập vào cân nặng (kg): "))
chieu_cao = float(input("Nhập vào chiều cao (m): "))
bmi = can_nang/(chieu_cao**2)
print("Chỉ số BMI:", bmi)
print("Dự báo:", end=" ")

if bmi < 18.5:
  print("Cân nặng thấp (gầy)")
elif 18.5 < bmi < 24.9:
  print("Bình thường")
elif 25 <= bmi:
  print("Thừa cân")
  if 25 < bmi < 29.9:
    print("Tiền béo phì")
  elif 30 < bmi < 34.9:
    print("Béo phì độ I")
  elif 40 < bmi:
    print("Béo phì độ III")




