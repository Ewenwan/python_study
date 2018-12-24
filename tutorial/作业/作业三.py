a = int(input('请输入一个数'))
b = int(input('请输入一个数'))
c = int(input('请输入一个数'))
max = a
if b > c:
    if max >=b:
        max = max
    else:
        max = b
else:
    if max >=c:
        max =max
    else:
        max=c
print('最大数是:',max)