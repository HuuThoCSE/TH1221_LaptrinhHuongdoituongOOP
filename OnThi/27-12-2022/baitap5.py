chuoi = 'Chao cau'
if '9' in chuoi:
    print("Có u trong chuoi")
else:
    print("False")

st = "Chao 2 cac 3 cau"
dc = 0
ds = 0
tu = 0
for kt in st:
    if kt.isalpha():
        dc+=1
    elif kt.isdigit():
        ds+=1
    if kt!=' ':
        tu += 1
print("Số chữ cái:", dc,". Số chữ số:", ds)
print("Có {} từ.".format(tu))

st = st.replace(" ", "-").upper()
print(st)

ds = [1, 2, 3, 4, 5, 6]
ds_chan = [x**2 for x in ds if x%2==0]
print(ds_chan)