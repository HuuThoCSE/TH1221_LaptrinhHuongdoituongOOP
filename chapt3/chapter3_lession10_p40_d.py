import string
e=0

mk=input("Nhập mật khẩu: ")
i=0
k=0
t1=0
t2=0
t3=0
t4=0

if len(mk)>=6 or len(mk)<=12:

    while i<len(mk):
        if  mk[i].isupper():
            t1+=1
        elif  mk[i].islower():
            t2+=1
        elif mk[i].isdigit():
            t3+=1
        elif mk[i] in "@" or mk[i] in "#" or mk[i] in "$":
            t4+=1
        i+=1

if t1==0 or t2==0 or t3==0 or t4==0:
        print("Mật khảu không hợp lệ")
else:
        print("Mật khẩu hợp lệ")