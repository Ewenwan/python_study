# 读 文本文件
"""
引题：ps、word 读写修改文件：美图秀秀把自己的照片美白加装饰；微博上上传本地图片；QQ上传本地表情图；管理系统上传excel批量导入信息。

# 场景：python 也可以读写文件。自动化和批量化，比如excel批量导入信息，比如批量修改图片元信息，比如批量保存头像，软件站自动下载软件。软件本质上也是代码对本地资源的读写。代替人工。

本地：指你自己的电脑，本地资源指C \D 盘上的资源。

纯文本文件：被计算机直接翻译并存储到硬盘上，只包含文字，没有特殊的效果格式。适合刚开始的读写研究。
"""

# 代码
file = open('english_ascii.txt', 'r')
content = file.read()
print(content)
file.close()


"""
读文件的流程：建立到文件的映射，生成文件对象 > 文件对象.读取信息 > 信息处理 > 关闭文件对象。

IO：input output 输入和输出， input()  print().

open：open(文件路径/文件名，模式)
'r'模式，read，读文件。

方法：文件对象.read() 读文件信息。file.close()  关闭文件，释放内存。

"""

# readline()
#
file = open('english_ascii.txt', 'r')
while True:
    content = file.readline()
    print(content)
    if content == '':
        break
file.close()


# readline()
file = open('english_ascii.txt', 'r')
content = file.readline()
print(type(content))
print(content)
for line in content:
    print(line)

"""
计算机文件读取原理：硬盘上的信息先读取到内存中，然后处理器处理内存中的程序展现信息。生活例子： 我准备开始做手工，首先要从混乱的房间把相关的工具（剪刀、螺丝刀）找出来，放到桌子上，然后再桌子上操作。这里房间相当于硬盘，桌子相当于内存。
持久化：把信息写入到硬盘中，断电也不会消失，信息是持久存在的。
流(stream): 计算机中存储是字节，读取文件就是读取众多字节组成的信息流。


f.read()   一次性全部读取信息到内存当中。缺点， 当文件较大时，这个过程耗费时间。
f.readline():  一次读一行。 生成器结构。有点，不占内存空间，速度快。缺点，不能再次从f对象读取信息。
f.readlines(): 一次性全部读取，返回一个列表，每一项是一行信息。优点：获得列表后方便操作。

转义字符\n告诉计算机换行。
"""





















