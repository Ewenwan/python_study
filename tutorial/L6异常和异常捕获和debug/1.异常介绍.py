# 异常介绍
"""
异常：代码写错了，解释器无法运行.主要包括书写上语法上的错误和运行时产生的错误。

从轻到重： 拼写检查insp<  普通information <警告warning < 运行时错误 runtime Error < 异常Exception < 严重的错误Error 崩溃
"""


# 2 错误栈
def foo():
    print(1/0)
def boo():
    print('hello')
    foo()
boo()
"""
错误跟踪栈  treaceback：错误栈展示出错信息 哪一个文件、第几行、出错的代码在哪个模块方法下、出错的代码。根据函数的嵌套和执行顺序，按从早到晚排序。最后是出错类型和描述。

如何出错：看看错误栈的前面的信息，知道从哪个代码开始出错；看看后面的信息，知道哪一句代码出错了：看看最后一句错误类型和描述。

""" 

# 3 遇到过的错误
"""
1)变量未声明就调用 print(a)   NameError：name'a'  is not defined
2)语法错误。少写冒号等。 SyntaxError: invalidsyntax
3) 缩进错误。  IndentationError: expected an indented block
4) 索引错误。[1,2,3] [3]。IndentationError:lise index out of range
5)类型错误。调用函数时参数的类型或个数不匹配。TypeError: foo() takes 0 positional arguments but 1 was given
6)值错误。 int('h') ValueError:lvalid liteal for int()wit base 10:'h'
7) 零除错误： 1/0。 ZeroDivisionError: division by zero
8)递归错误。RecursionError: maximun recursion depth exceeded
9) 键错误    {'key':'value'}['aaa']   KeyError:'aaa'
...
"""