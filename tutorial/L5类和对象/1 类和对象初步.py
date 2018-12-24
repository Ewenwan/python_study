# 初始类和对象

# 引题:回忆之前没有函数是的写法，有函数封装后的写法。
#1.单条语句
r1 = 3
r2 = 4
r3 = 5.5
print('圆的面积:',r1*r1)
print('圆的面积:',r2*r2)
print('圆的面积:',r3*r3)
# 2. 函数         封装功能，抽象出解决问题的公共过程。调用时传入真实数据。
def calcylate_square(r):
    return r*r
calcylate_square(r1)
calcylate_square(r2)
calcylate_square(r3)

#  2. 函数
stu1 = {'name':'小明','score':98}
stu2 = {'name':'小红','score':80}
def print_stu_info(stu):
    print('学生{}成绩{}'.format(stu['name'],stu['score']))
print_stu_info(stu1)
print_stu_info(stu2)

# 2.函数.面向函数思想
print('起床')
print('吃早餐')
print('上班')
print('下班')

# 2.函数   学生管理作业，先获取用户输入，(假设用户要修改学生) 先展示学生列表，再接收用户输入新学员的信息，再代码修改数据，最后提示修改成功。

# 3. (常用)向对象
class Student():
    def __init__(self,name,score,sex):
        self.name = name
        self.score = score
        self.sex = sex

    def print_score(self):
        print('{}的成绩是{}'.format(self.name,self.score))

    def print_sex(self):
        print('{}的性别是{}'.format(self.name,self.sex))
# 实例化
stu1 = Student('小明', 90, '男')
stu2 = Student('小红', 100, '女')
# 调用对象方法
print(stu1.name)
stu1.print_score()   #本质Student.print_score(stul)
stu2.print_sex()

"""
对象object：python万物皆对象，字符串、数字、方法、类实例。
类class：相似、有公共特征的一类对象。
类class和实例instance: “人类”和“小明”。类是许多个体的集合，一个抽象名词、统称。'小明' 或者“你自己”或者“普特朗” 这些都是人类这个集合中一个个具体的人、个体。那么我们把类中具体的个体叫“对象”、“实例”。再举几个例子：水果类包含苹果、梨。电子产品类，电脑，手机。手机类，苹果，华为
属性attribute，成员方法：一类事物的特性叫做属性，例如Student类中的name、score、sex。类中个体、成员具备的功能、方法叫做成员方法

语法：类关键字class  类名():   类方法。
驼峰命名:(约定俗成) 每一个单词挨着写并且首字母大写。例如：Electronic_product。java中常见。


__init__():  双下划线开头的方法为内置或特殊用途方法。
__init__()又叫做“构造函数”。initial 初始化。
类实例化的时候调用__init__()函数。实例化传入的参数传入init函数，init函数内又赋值给了self对象。为了生成、构造、写信息到一个具体的实例。
self: 自己  指代类自己的某一个实例。好像函数里的形参。类里面的每一个函数，都默认传递self参数，self要写在参数的第一位。对象方法调用时，不用传递self参数。
属性、成员方法：访问属性  对象.属性名：调用成员方法  
实例.方法：写属性  对象.属性名=新值。成员方法把实例中的属性读出来并书写功能。

封装: 类的三大特性之一。类的封装比函数的封装更加抽象高级，因为类不光包括功能，还包括数据结构。

面向过程（函数）和面向对象：
面向过程，解决一个问题，先干什么后干什么，计划步骤。
面向对象，把数据结构和业务逻辑看做一个整体，对同类对象抽象共同特征写成类，暴露简单的接口与外界交互，而不需要考虑细节。
"""












