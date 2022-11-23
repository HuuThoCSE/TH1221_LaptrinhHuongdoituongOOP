import string
c=input("Nhập chuỗi: ")
dkc =int(0)
ds=int(0)
s=""
for i in range (0,len(c)):
    if c[i].isalpha()!=1:
        dkc+=1
print("Có ",dkc," không phải chữ cái")
c=c.upper()
print(c)
for i in range (0, len(c)):
    if c[i].isalpha()!=1:
        ds+=1
cs="0123456789"
max=int(0)
for i in range (0,len(cs)):
    dsl= int(0)
    for x in range (0, len(c)):
        if cs[i] in c[x]:
            dsl+=1
    if max < dsl:
        max = dsl
        s=cs[i]



print("Số ",s, " được lặp lại nhiều nhất với ", max, " lần." )
