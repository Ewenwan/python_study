# 类变量和静态方法

# 引题：函数封装版的学生管理系统，业务相关方法应该会改装成类封装的成员函数，但全局变量student_list不知道放到哪里。

# 示例
class Student():
    student_list = ['小明','小红']      # 类变量

    def __init__(self,name):
        self.name = name        # 属性，对象变量。
        Student.student_list.append(self.name)

    def print_name(self):       # 对象方法
        print('学生姓名{}'.format(self.name))

    @staticmethod      #@classmethod
    def how_many(cls):        # 静态方法。针对整个类，不需实例化。
        #判断类内一共多少个学生
        print('学生总人数:{}'.format(len(cls.student_list)))

    def __del__(self):
        print('实例被销毁')

stu_xiaoli = Student('小李')
stu_xiaoli.print_name()
stu_xiaoli.how_many()
print(Student.student_list)       # 调用类变量。  类.类变量
Student.how_many()    # 静态方法调用。 类.静态方法

# 命名空间(了解)： 类封装之后，没个类隔离，可以起相同的属性名，例如name。这样的话，当你引用一个变量，需要告诉解释器这个变量从哪一个大区域来的，这个区域叫做命名空间。我们平时用的print()、def关键字其实属于built-in空间。以后还会学到模块、包、蓝图，本质都相当于文件夹。

# 对象变量(类的属性)：思维角度针对一个实例、对象。例如self.name中的name。要先实例化，然后再对对象变量进行读写。pritnt_name()对象方法也是针对实例的。

# 类变量：思维角度针对整个类。写在类内部。作用域 整个类内使用。语法  类名.变量名。好像学函数时函数外的全局变量。
# 引题，需求写一个how_many()函数，返回学生列表长度，传统写法how_many(self)   stu_xiaoli.how_many()。缺点：必须要先实例化，但是这一句代码麻烦且不必要，思维上也不顺，因为how_many方法针对的是学生类而不是具体学生。

"""
静态方法 static：静态的意思是一直存在在内存当中，可以随时调用，全局的，不会动态新生成和销毁。类中的静态方法不需要实例化就可以随时调用。

staticmethod装饰器：静态方法通过@staticmethod或@classmethod实现，两个装饰器区别，staticmethod不需要self、cls参数。@classmethod第一参数cls代表类自己，可以在被修饰的方法中调用类自己的变量和方法。

cls：当使用@classmethod装饰器的时候，方法的一个参数是cls而不是self。cls （缩写class）就好像self形参指实例，只是cls指代的是类(代指上例Student类)。cls的好处是代指类名，好像形参一样，如果类名变化类中代码不需要修改。类似于java中的this。
"""

"""
析构函数：类实例化调用构造函数__init__(),开辟了内存空间。实例不再被使用后，调用__del__()回收实例。__del__自动调用平时不需要写。
"""