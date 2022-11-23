# 4. Viết chương trình nhập vào điểm trung bình chung của 1 sinh viên theo thang điểm 4,
# hãy cho biết sinh đó được xếp loại gì?

diem = float(input("Nhập điểm trung bình theo thang điểm 4: "))
print("Xếp loại:", end=" ")
if diem < 1:
  print("Kém.")
elif 1 <= diem <= 1.99:
  print("Yếu.")
elif 2 <= diem <= 2.49:
  print("Trung bình.")
elif 2.50 <= diem <= 3.19:
  print("Khá.")
elif 3.20 <= diem <= 3.59:
  print("Giỏi.")
elif 3.60 <= diem <= 4:
  print("Xuất sắc.")