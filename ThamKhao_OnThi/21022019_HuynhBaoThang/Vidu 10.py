f2 = open('Lthđt.txt','w',encoding='utf-8')
f2.write('Học phần: LẬP TRÌNH HĐT\n')
f2.write("Số tín chỉ: 3\n")
f2.write('Thực hành trên NNLT: Python')
f2.close()
f2 = open('Lthđt.txt','r',encoding='utf-8')
nd = f2.read()
print(nd)
f2.close()