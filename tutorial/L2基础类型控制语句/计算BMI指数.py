#练习一 计算BMI指数

# 用户输入
height = input('请输入身高(cm):')
weight = input('请输入体重(kg):')
height = float(height)
weight = float(weight)

# 计算bmi
bmi = weight / (height/100 * height/100)
print(bmi)

# if判断
if bmi < 18.5:
    print('体重偏轻')
elif 18.5 <= bmi < 23.9:
    print('正常')
elif 23.9 <= bmi < 32:
    print('偏重')
elif bmi >= 32:
    print('超重')
