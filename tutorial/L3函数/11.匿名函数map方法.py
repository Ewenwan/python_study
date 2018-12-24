# 匿名函数
# 引题： 计算某个数的平方值
def square(n):
    n = n*n
    return n * n

print(square(3))

# 关键字lambda，语法糖，跟上面def定义的函数功能语法一致。匿名函数没有名字，没有函数，有形参，有return语句。
# lambda 后面跟的是返回值 相当于普通写法的return，冒号后面跟的是表达式，相当于普通写法return后面的表达式
# 好处，可以写成单行，更加简洁，与其他表达式连用。
lambda x: x*x
f = lambda x: x*x        # 没有名字的函数，我想调用它，先把它赋值给一个变量。
print(f(3))

# 场景：适合不太复杂的函数和跟其他表达式连用。


# 2,map方法
# 语法;map(方法，可迭代列表) ,依次把可迭代对象中每一项的值带入到方法中进行计算，返回值是map对象 (结果列表)
# 方法也可以作为形参
def square(n):
    return n*n

for i in map(square(square,[1,2,3])):
    print(i)

map(square,[1,2,3])   # [1,4,9]

# 相当于传统方法
# new_list = []
# for i in [1,2,3]:
#     num_square = square(i)
#     new_list.append(num_square)
# print(new_list)

# map跟匿名函数连用
map(lambda x: x*x,[1,2,3])