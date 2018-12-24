# 判断变量类型

#类型不同，input()返回字符串
#'1' + 3       '小明考了' + 90  报错

#type()   判断变量类型
a = 1
b = 1.5
c = 'hello'
type(a)     # <class 'int'>
type(b)     # <class 'float'>
type(c)     # <class'str'>
type(d)     # <clss 'bool'>



# isinstance(值，类型)
# 如果值属于类型的话返回True
isinstance(1,int)  # True
isinstance(1,int)  #False
isinstance('小明',float)  # False