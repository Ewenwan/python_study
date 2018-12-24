# 参数

#
def myday():
    print('起床')
    print('吃早餐')
    print('上班')
    print('下班')
    print('睡觉')






# 一个参数的函数
def calculate_area(r):
    print('圆面积',3.14 * r * r)

calculate_area(5)

def calculate_absolute(num):
    if num < 0:
        return -num
    if num > 0:
        return num
print('绝对值',calculate_absolute(5))
print('绝对值',calculate_absolute(-3))

# (了解) 常用的内置之一。注意变量名不要用内置关键字或函数。
print(abs(-3))
print(max(1,5,3))
print(min(1,5,-2))



# 多个参数的函数
def get_max(a, b, c):
    max_num = a

    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c

    return max_num
get_max(1, 5, 3)


# 参数 argument：函数运行前需要告诉函数一些运行时需要的信息原料，数值，函数根据传入的参数：参与内部的逻辑运算。
# 形参：函数定义的时候。占位、将要传进数值的“形式上的代表”。形参名可变，我们只关注形参的类型。
# 实参：函数调用的时候。传入函数的“实际具体数值”。注意实参的值要与形参的个数、类型保持一致。

# 可能出现的错误：实参和形参个数或类型不一致报错。