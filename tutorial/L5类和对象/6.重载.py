# (了解)  重载
# 面试题：重写跟重载的区别?
# 重写参考  L5/5类的继承2.py一节

# 引题1：写几个关于比大小的函数。
# 1> 给定两个数，返回最大的那个数

# 3> 传入数字组成的列表[1,0,-1,3.5]，返回最大的那项数字
def get_max(num1,num2):
    # if num2 > num1:
    #     return num2
    # else:
    #     return num1
    max = num1
    if num2 > max:
        max = num2
    return max

print(get_max(1,3))
# 2> 给定三个数，返回最大的那个数
def get_max2(num1,num2,num3):
    max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3
    return max_num

print(get_max2(4,5,6))



def get_max3(num_list):
    max = num_list[0]
    # for i in range(0,len(num_list)):
    #     if max < num_list[i]:
    #         max = num_list[i]
    for index,num in enumerate(num_list):
        print(index,num)
        if num > max:
            max = num
    return max

num_list=[4,5,6,-1]
print(get_max3(num_list))



# 把上面的三个函数封装到一个类中
class GetMaxNum(object):
    @staticmethod
    def get_max(num1, num2):
        max = num1
        if num2 > max:
            max = num2
        return max

    @staticmethod
    def get_max2(num1, num2, num3):
        max_num = num1
        if num2 > max_num:
            max_num = num2
        if num3 > max_num:
            max_num = num3
        return max_num

    @staticmethod
    def get_max3(num_list):
        max = num_list[0]
        for index, num in enumerate(num_list):
            print(index, num)
            if num > max:
                max = num
        return max


print('最大值',GetMaxNum.get_max1(1,3))
print('最大值',GetMaxNum.get_max2(1,3,2))
print('最大值',GetMaxNum.get_max3([1,3,2]))



"""
重写；子类重写父类中的同名方法。
重载：类中有多个同名方法，参数个数不同，或参数类型不同，这种情况较方法重载。针对方法参数的不同情况。

python当中没有重载机制。同名函数重复定义，以最后的为准。因为python是动态类型语言，传实参什么类型都接收；形参和实参可以传可变个数的参数。
"""
