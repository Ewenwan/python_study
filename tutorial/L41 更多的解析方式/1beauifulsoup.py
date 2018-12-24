# beautifulsoup
# bs包把html按照节点的层级关系转换为树形文档，然后解析，简单易用
# 安装 pip install beautifulsoup4   注意beautifulsoup只能用于py2
# lxml 是安全解释html标签到文档树 支持bs和path
# 安装 pip install lxml
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <a id="aaa"href='http://www.baidu.com' name='aaa'
        class="aaa">百度一下</a>
        <a href='http://www.baidu.com'>百度一下2</a>
        <h1>大家好</h1>
    </body>
</html>
"""
# 实例化bs 传入参数待解析html内容和解析器
# html.parser python内置，方便兼容性好，lxml基于c 效率高 需要安装包
bs = BeautifulSoup(html,'lxml')
# bs1 =BeautifulSoup(html,'html.parser')
# prettify格式化输出
print(bs.prettify())

# 查找标签
print(bs.head) # 不存在返回None
print(bs.a)   # <a class="aaa" href="http://www.baidu.com" id="aaa" name="aaa">
print(bs.find_all('a')) # <a>....</a>

#标签名称
print(bs.name)
print(bs.a.name)

# 标签属性
print(bs.a['href'])

# 了解 删除标签属性
print(bs.a)
del bs.a['id']
print(bs.a.attrs) #{'href': 'http://www.baidu.com', 'name': 'aaa', 'class': ['aaa']}

# 标签内容
print(bs.a.string) #百度一下

# 子节点和父节点
print(bs.body.contents) # 返回列表标签下所以子标签的内容
print(bs.body.children) #返回迭代器中字节
a=bs.body.children
for c in a:
    print(c)


#搜索
print(bs.find_all('a'))
print(bs.find_all(['a','h1']))

# 搜索 根据属性
print(bs.find(id='aaa'))
# 根据class 了解即可
print(bs.find_all(claa='aaa'))
# 根据css语法 了解即可
print(bs.select('a'))
print(bs.select('.aaa'))
print(bs.select('#aaa'))
print(bs.select('body.aaa'))