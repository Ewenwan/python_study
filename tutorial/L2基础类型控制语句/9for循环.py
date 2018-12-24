# for循环

for n in [1,2,3,4,5]:
    print(n)

# for 变量 in 可迭代对象：  变量每一次循环都会等于对象中一项。
# 遍历： 依次访问到 可迭代对象中的每一项。
# 可迭代对象：可以被遍历的对象。  例如列表，字符串，序列

for n in [1,2,3]:
    print('hello')

# range()
for n in range(1,10):      # 1,2,3,4,5,6,7,8,9   [1,10)
    print(n)
# range(起始值，结束值,步进)， 返回一个序列,左闭右开区间

for n in range(1,10, 2):
    print(n)


# 循环嵌套
for x in range(1,5):
    for y in range(1,5):
        print(x,y)