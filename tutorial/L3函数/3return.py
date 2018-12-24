# 函数的返回值
# 1.带返回值的函数
def get_max(a,b,c):
    max_num = a     # 存储最大值

    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c

    return max_num

max_number = get_max(1,5,3)
print('最大值',max_number)
print(get_max(-2,4,90))
# 函数的返回值：参数进入函数，经过业务逻辑处理，返回处理后的结果。
# 返回值以关键字return开头，可以返回数字、字符串、布尔。
# 函数一般明确返回值，设计上应该计算逻辑和业务逻辑分离开。建议返回明确的值。没有返回值的函数默认返回None。

# 易错点：函数中没有print()，函数调用后终端看不到结果，因为接受并打印函数的返回值。


# 2.不带返回值的函数，只是一些功能的封装
def myday():
    print('起床')
    print('吃早餐')
    print('上班')
    print('下班')
    print('睡觉')

# 3.返回多个值的函数
def get_max_min(a,b,c):
    max_num = a
    max_min = a

    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c

    if b < max_min:
        max_min = b
    if c < max_min:
        max_min = c

    return max_num,  max_min

num1,num2 = get_max_min(1,5,3)
print('最大值{}最小值{}'.format(num1,num2))
# 函数可以有多个返回值，return的时候逗号隔开
# 析构赋值、解包赋值：函数返回多少个值，就用多少个变量去接收，顺序一致。