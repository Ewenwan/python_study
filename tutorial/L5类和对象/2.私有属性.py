# 私有属性

# 1 引题
# class Student():
#     def __init__(self,name,score,sex):
#         self.name = name
#         self.score = score
#         self.sex = sex
#
#     def print_score(self):
#         print('{}的成绩是{}'.format(self.name,self.score))
#
#     def print_sex(self):
#         print('{}的性别是{}'.format(self.name,self.sex))
# # 实例化
# stu1 = Student('小明', 90, '男')
# stu2 = Student('小红', 100, '女')
# # 调用对象的属性
# print(stu1.name)
# print(stu1.score)
# print(stu2.name)
# print(stu2.score)
# # 写属性
# stu1.score = 100
# print(stu1.score)

#上面的例子说明类的属性可以读也可以被修改。但是这样会导致安全问题，比如小明修改成绩。类内部保密只需要暴露跟外部通信的接口。外部不应该直接修改类的属性。

# 2. 私有变量
class Student2():
    def __init__(self,name,score,sex,password):
        self.__name = name
        self.__score = score
        self.__sex = sex
        self.__password = password

# stu1 = Student2('小明', 90, '男','123456')
# print(stu1.__password)
# 双下滑线开头的属性不能直接访问，这样确保了安全性。
# 访问私有属性会报AttributeError: 'Student2' object has no attribute '__password'
# 但是有的时候我们又想获取对象的信息。

# 3. getter函数
class Student3():
    def __init__(self,name,score,sex,password):
        self.__name = name
        self.__score = score
        self.__sex = sex
        self.__password = password

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if score < 0 or score > 100:
            raise ValueError('分数输入错误')
        self.__score = score

stu1 = Student3('小明', 90, '男','12345')
print(stu1.get_score())
stu1.set_score(100)
print(stu1.get_score())

# stu1.__score = 100    #  私有属性不能被直接修改
# print(stu1.get_score())  #
# java中类每个属性都有getter setter方法。
#getter和setter函数可以提供更加精细的控制。

# 4. (了解)property装饰器
# 因为上面的getter setter
class Student3():
    def __init__(self, name, score, sex, password):
        self.__name = name
        self.__score = score
        self.__sex = sex
        self.__password = password
        # self.score = score()

    @property  # getter_score
    def score(self):
        return self.__score

    @score.setter  # setter_score
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('分数输入错误')
        self.__score = score


stu1 = Student3('小明', 90, '男', '12345')
print(stu1.score)
stu1.score = 98



