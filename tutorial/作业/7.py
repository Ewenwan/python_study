#n = int(input('请输入一个整数:'))
#for i in range(2, n):
#    if n % i == 0:
#        print('%d 不是质数' % n)
#        break
#else:
#    print('%d 是质数' % n)

#7
num = 7    # 待判断的数
total = 0  # 可以整除的次数

if num == 1:
    print('1既不是质数也不是合数')

for i in range(1,num+1):
    if num % i == 0:
        total = total + 1


# 能被1和自身整除
if total == 2:
    print(num,'质数')
# 能被1、自身、和其他数整除
elif total > 2:
    print(num,'合数')
