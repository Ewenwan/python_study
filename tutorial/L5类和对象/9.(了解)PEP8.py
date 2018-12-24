# (了解)PEP8代码风格指导


"""
PEP  Python Enhancement Proposal   ,python相关功能官方声明。
PEP8 意思 python官方第8号文件，这个文件说明了python语言代码应该怎么书写，指导了书写风格。当你的代码没有做到文件要求的时候，pycharm会报灰线轻度提示。没有完全遵守规则不影响代码执行。但建议遵守。
"""

# 操作符前后应该有一个空格
a=3
a = 3
# 方法与方法间有两个空行
def foo():
    pass


def boo():
    pass
#类中的方法相隔一行
class Student(object):
    def foo(self):
        pass

    def boo(self):
        pass

# 类与类之间空两行
# 如果父类没有不写括号
# 类名应该用驼峰风格
class aaa():
    pass


class Bbb:
    pass
# 方法名、类名不要重复使用
def boo():
    pass
# 两个条件有时可以写成链式的
if 1<a and a<2:
    pass
if 1 < a < 2:
    pass
# 不建议代码写的过长，80个字符。python的提示灰线在120字符
# 来看待今飞凯达深V看离开那里可能来看看你可男可女你看弄好发一套房源鱼头空间看看科技板块卡通人虽然他的从时和
# 文件末尾代码时另起一新行
print('end')
# 字典冒号后有空格，括号前后无空格
print({'name':'小明','age':13})

"""
python有关代码风格操作
1.界面右下角图标点击，调节提示出现的级别（不提示、语法、拼写）
2.自动格式化代码快捷工具，界面左上菜单code/reformat  code 。
"""

"""



"""