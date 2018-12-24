# 包引用
"""
包 package：组织各个py脚本文件和其他配置、静态文件等，项目由包组成的，确定项目组织的层次结构。说白了就是写好的代码。封装。
内置包：除了pypi网站，python解释器已经内置了一些常用的包，可以安装目录/Lib sitepackages目录下看到。
第三方包：程序员上传到pipy网站上的包，直接拿来用，而不需要从头开发，大大提高了开发效率。
包的好处：组织项目结构清晰；命名空间隔离，不同包下可以有同名文件。


__init__.py :  包类似windows资源管理器上的文件夹。只是这个文件夹下有一个__init__.py的文件夹。

一个包下必须要有__init__.py，__init__.py 可以为空。
__init__.py  作用：
1. 说明是一个包而不是一个文件夹。
2. 控制包的具体行为，功能比文件夹更加，相当于升级版文件夹。
3. 项目初始化逻辑，例如声明类的实例；初始化数据库连接；初始化项目运行环境。


"""



"""
引用语法 (import  引入)

执行import语句时，python解释器会自动在包安装目录下查询同名包。
 1. import 包名  ：引用包中的所有py文件。
 2. form 包名  py 脚本 import 脚本中类，方法，变量 ： 用什么引什么
 简写from  包名.py脚本  import *
 3. from 包.子包  import  子包里的py脚本。
 
查找路径：import包的时候，python解释器首先从项目跟目下开始查找符合的包名如果未找到再去 解释器安装目录/Lib、安装目录/Lib/sitepackages  目录下查找内置包或三方包。
"""

"""
__name__:内置的特殊值，返回文件名。
1. 当.py自己执行时， 它的值为 '__main__',表示主函数、入口文件
2. 当.py被另一个脚本文件import时，__name__的值为
包层级结构.文件名 。

if __name__ == '__main__': pass

场景：.py文件中有写好的类、函数、测试代码。当这个.py文件被引用时，我们希望引用写好的业务逻辑，但不希望执行测试代码。可以把跟这个.py文件相关但跟项目无关的测试代码放到if __name__ == '__main__': 下面。
"""








