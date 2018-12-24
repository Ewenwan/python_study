from L8包.package.pack1 import py1   # 绝对路径
from . import py1    # 相同路径   同级路径
from ..import pack1    # 父级目录。py2.py在pack1目录下，pack1的父目录是package包目录下，所以可以引用package包下的内容。
from ..pack1 import py1