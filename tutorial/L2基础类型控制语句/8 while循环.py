# while循环
# if True:
#    print('hello')

while True:
   print('hello')
"""
while<条件>:
    如果条件为True,那么重复执行while语句块中的内容。

 如果while循环的条件一直未True,死循环。
"""
# while True:
#    numbe = 20
#   user_number = int(input('请猜一个数字：'))
#
#    if user_number < number：
#         print('猜小了')
#     elif user_number > number:
#        print('猜大了')
#    else:
#        print('猜对了')

num = 0
while num < 10:
    print(num)
    num = num + 1
    num +=1    # 简写语法
