# 写文本文件


# 回忆读取文本文件示例
# file = open(fole='chinese_utf-8.txt',mode='r',encoding='utf-8')
# content = file.read()
# print(content)
# file.close()

# 写文件
file = open('write.txt','w',encoding='utf-8')
file.write('hello world')
file.write('小明')
file.write('\n')
file.write('天黑的开始早了')

file.writelines(['第一行','second line','第三行'])

"""
写入文件 open函数先打开一个空文本文件。
模式为'w'，意为write 写。如果文件名不存在，执行代码会自动新建。
utf-8 UTF8 utf_8 这些写法都行。同理ascii  ASCII gbk GBK 都可以。

"""


