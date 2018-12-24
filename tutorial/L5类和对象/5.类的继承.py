# 类的继承

"""
引题：生活例子。手机类，OPPO手机、华为手机看做是手机类里的对象；但oppo手机也可以称作一个类，这个类下又包含find系列、R系列，R系列类又包含某某具体型号对象。类有包含、继承的关系。
"""

# 引题2：写一个教师类：属性name age sex salary subject sddress phone，方法say_hi()，go_work(),
# 再写一个学生类：属性name age sex hobby parent info,方法say_hi(),go_class()。
# 再写行政人员类
class Teachar():
    def __init__(self,name,age,sex,salary,subject,address):
        self.name = name
        self.age = age
        self.sex = sex
        self.salary = salary
        self.subject = subject
        self.address = address

    def say_hi(self):
        print('hello')

    def go_work(self):
        pass

class Student():
    def __init__(self,name,age,sex,hobby,parent_info):
        self.name = name
        self.age = age
        self.sex = sex
        self.hobby = hobby
        self.parent_info = parent_info

    def say_hi(self):
        print('hello')

    def go_class(self):
        pass

# 上面的代码类与相似的类有重复的属性、方法，书写麻烦。
# 所以python引入了类继承机制。继承是类的三大特性之一。


"""
父类：上例中 Animal类逻辑上、范围上包含dog、Cat类。那么我们把 Animal类叫做
“父类”、“超类”、“基类”；Dog、Cat类就叫做“子类”、“衍生类”

继承：语法 类定义时，类名后面小括号里面填写父类名。注意跟类实例化时、函数后面的小括号里面的内容不一样。

object：python中变量、方法万物皆对象，现实生活中也是万物皆对象。为了面向对象体系完整，定义了一个默认的、抽象的顶级对象object。object是所有类的父类。每一个类都默认继承object类，具备一些关于类的基础方法如__init__  __del__。

子类继承父类的属性、方法：Dog类实例化用的是父类Animal类中的__init__()   run()。例如华为手机类拥有的父类手机类打电话、发短息功能。

场景：类比较多而且相似的时候，适合抽象为父类、子类，比如游戏。过度抽象可能会使问题更加复杂，不要刻意去使用父子类。
好处：类与类关系更加清晰；代码量少；公共部分抽象出来，扩展更加方便。
"""







