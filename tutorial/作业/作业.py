a = input("请输入：")
b = 0
c = 0
d = 0
e = 0
for i in a:
    if i.isalpha():
        b += 1
    elif i.isdigit():
        c += 1
    elif i.isspace():
        d += 1
    else:
        e += 1
print("字母{}个，数字{}个，空格{}个，特殊字符{}".format(b,c,d,e))

