str="Nguyen%Huu$Tho12324444334"
# str=input("Nhập vào chuỗi bất kỳ: ")
Count_0 = 0
Count_1 = 0
Count_2 = 0
Count_3 = 0
Count_4 = 0
Count_5 = 0
Count_6 = 0
Count_7 = 0
Count_8 = 0
Count_9 = 0

for i in range(0, len(str)):
    if str[i] == '0':
        Count_0+=1
    elif str[i] == '1':
        Count_1+=1
    elif str[i] == '2':
        Count_2+=1
    elif str[i] == '3':
        Count_3+=1
    elif str[i] == '4':
        Count_4+=1
    elif str[i] == '5':
        Count_5+=1
    elif str[i] == '6':
        Count_6+=1
    elif str[i] == '7':
        Count_7+=1
    elif str[i] == '8':
        Count_8+=1
    elif str[i] == '9':
        Count_9+=1

max_value = 0
KeyMax = 0
if Count_0 > Count_1 and Count_0 > Count_2 and Count_0 > Count_3 and Count_0 > Count_4 and Count_0 > Count_5 and Count_0 > Count_6 and Count_0 > Count_7 and Count_0 > Count_8 and Count_0 > Count_9:
    KeyMax = 0
    max_value = Count_0

elif Count_1 > Count_0 and Count_1 > Count_2 and Count_1 > Count_3 and Count_1 > Count_4 and Count_1 > Count_5 and Count_1 > Count_6 and Count_1 > Count_7 and Count_1 > Count_8 and Count_1 > Count_9:
    KeyMax = 1
    max_value = Count_1

elif Count_2 > Count_0 and Count_2 > Count_1 and Count_2 > Count_3 and Count_2 > Count_4 and Count_2 > Count_5 and Count_2 > Count_6 and Count_2 > Count_7 and Count_2 > Count_8 and Count_2 > Count_9:
    KeyMax = 2
    max_value = Count_2

elif Count_3 > Count_0 and Count_3 > Count_1 and Count_3 > Count_2 and Count_3 > Count_4 and Count_3 > Count_5 and Count_3 > Count_6 and Count_3 > Count_7 and Count_3 > Count_8 and Count_3 > Count_9:
    KeyMax = 3
    max_value = Count_3

elif Count_4 > Count_0 and Count_4 > Count_1 and Count_4 > Count_2 and Count_4 > Count_3 and Count_4 > Count_5 and Count_4 > Count_6 and Count_4 > Count_7 and Count_4 > Count_8 and Count_4 > Count_9:
    KeyMax = 4
    max_value = Count_4

elif Count_5 > Count_0 and Count_5 > Count_1 and Count_5 > Count_2 and Count_5 > Count_3 and Count_5 > Count_4 and Count_5 > Count_6 and Count_5 > Count_7 and Count_5 > Count_8 and Count_5 > Count_9:
    KeyMax = 5
    max_value = Count_5

elif Count_6 > Count_0 and Count_6 > Count_1 and Count_6 > Count_2 and Count_6 > Count_3 and Count_6 > Count_4 and Count_6 > Count_5 and Count_6 > Count_7  and Count_6 > Count_8 and Count_6 > Count_9:
    KeyMax = 6
    max_value = Count_6

elif Count_7 > Count_0 and Count_7 > Count_1 and Count_7 > Count_2 and Count_7 > Count_3 and Count_7 > Count_4 and Count_7 > Count_5 and Count_7 > Count_6 and Count_7 > Count_8 and Count_7 > Count_9:
    KeyMax = 7
    max_value = Count_7

elif Count_8 > Count_0 and Count_8 > Count_0 and Count_8 > Count_1 and Count_8 > Count_2 and Count_8 > Count_3 and Count_8 > Count_4 and Count_8 > Count_5 and Count_8 > Count_6 and Count_8 > Count_7 and Count_8 > Count_9:
    KeyMax = 8
    max_value = Count_8

elif Count_9 > Count_0 and Count_9 > Count_1 and Count_9 > Count_2 and Count_9 > Count_3 and Count_9 > Count_4 and Count_9 > Count_5 and Count_9 > Count_6 and Count_9 > Count_7 and Count_9 > Count_8:
    KeyMax = 9
    max_value = Count_9

print("Chữ số xuất hiện nhiều nhất", KeyMax, "với số lần xuất hiện là", max_value)