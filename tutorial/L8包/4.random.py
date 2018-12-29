#  random    随机
import random

# random()     0到1之间生成一个随机数,这个函数的结果乘以100可以其他范围内的随机数。
print(random.random())

# 随机数如何产生：cpu主频，cpu温度，鼠标滑动轨迹 等等。

# randint()      起止范围内的随机整数，左闭右闭区间。
print(random.randint(1,100))

# choice   从可迭代对象中随机选一个元素
print(random.choice([1, 2, 3, 4]))

# shuffle  洗牌
list1 = [1, 2, 3, 4]

print(list1)





