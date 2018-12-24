# 用户输入
km = input('输入公里数')
km = int(km)

pay = 0     #花费

if km <= 2:
    pay = 8
elif 2 < km <= 12:
    pay = 8 + (km-2)*1.2
elif km > 12:
    pay = 8 + 10*1.2 + (km-12)*1.5
else:
    print('输入不合法')

# 打印结果
print('花费一共' + str(pay) + '元')