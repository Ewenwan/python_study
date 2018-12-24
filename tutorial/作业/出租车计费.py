#出租车计费


kilometre =''
money = ''
kilometre = input('请输入公里数(km)')
kilometre = float(kilometre)
if kilometre <= 2:
    money = 8
elif kilometre <= 12:
    money=8+1.2*(kilometre - 2)
else:
    money = 8 + 1.5 * (kilometre - 12) + 1.2 * 10
print(money)

