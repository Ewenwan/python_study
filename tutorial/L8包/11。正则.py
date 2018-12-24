# （爬虫 django之前讲）
# 需求 给你一个网站一个页面的源代码，要求吧网址都选出来，返回列表。find可以做但麻烦，复杂了就不好做。
#  正则:re  regex。专业做字符串查找筛选。比''.find()强大的多。有自己专用的语法。优点：功能最为强大。缺点学习曲线曲折。
# 场景：爬虫、网页解析。匹配，flask django 框架基于的路由就是正确的
#regex  三方包 功能比内置的re包更强大
# 前缀r，raw原始字符串，运行中不需要处理转义字符。
import re

# 简单但功能有限不方便
html =r'<html><boby><h1>多捞啊，world</h1></boby></html>'
start_index=html.find('<h1>')
end_index=html.find('</h1>')
print(html[start_index:end_index])

#1>匹配固定字符串一次
# (爬虫 django之前将)
#  需求：给你一个网站一个页面的源代码，要求把网址都选出来，返回列表。 ''.find()可以做但很麻烦。如果需求复杂find不能胜任
# # 正则：re regex 。专业做字符串查找筛选。比''.find()强大的多。有自己专用的语法。优点: 功能最为强大。缺点学习曲线陡峭。
# 场景：爬虫、网页解析。匹配、flask django框架的路由就是基于正则的。
# regex 三方包，功能比内置的re包更强大。
# 前缀r，raw原始字符串，运行中不需要处理转义字符。

import re

# find()     简单但功能有限不方便
html = r'<html><body><h1>hello world</h1></body><ml>'
start_index = html.find('<h1>')
end_index = html.find('<h1>')
print(html[start_index: end_index+1])

# 1> 匹配固定字符串1次
key1 = r'javapython1asdfghjklpython'
pattern1 = re.compile(r'python')
matcher1 = re.search(pattern1,key1)
print(matcher1)
print(matcher1[0])
# compile(正则规则)  返回包含规则的匹配器对象。
# re.search(匹配器对象，待查找字符串)

#2.>任意字符串 .匹配任意字符 +修饰前面的匹配规则重复一次或多次
key2 =r'<h1>hello world</h1>'
pattern2=re.compile(r'<h1>.+</h1>')
matcher2=re.search(pattern2,key2)
print(matcher2[0])
print(matcher2)


#3》 匹配 点 加号
key3=r'1417633855@qq.com'
p3 = re.compile(r'.+@qq.com')
m3 = re.search(p3,key3)
print(m3[0])

# 4.
key4= r'http://www.baidu.com https://www.baidu.com'
p4 = re.compile(r'https*://')
m4 = re.search(p4,key4)
matcher4 = p4.findall(key4)
print(matcher4)
# 匹配器.findall(带匹配字符串 返回列表)

# 5.匹配一个字符，大小写有一个匹配到了就可以
key5 =r'selectSELECT'     # sql大小写不敏感
p5=r'[sS][eE][Ll][Ee][Cc][tT]'
p5 =re.compile(p5)
print(p5.findall(key5))

# 6.》 排除
key6 =r'mat cat hat pat'
p6=re.compile(r'[^p]at')
print(p6.findall(key6))

# 7.
key7 =r'1417633855@qq.com.cn'
p7 = re.compile(r'.+@.+\..+\.')
print(p7.findall(key7))

#8. 惰性匹配  符合任意字符的情况下 字符最少的。
p8 = re.compile(r'.+@.+?\.')
print(p8.findall(key7))

# 9.匹配固定次数
key9 =r'saas sad sads sad sdassd'
p9 =re.compile(r'sa{1,2}s')
print(p9.findall(key9))

#10》匹配换行后的内容 re S
key10="""
aaaa
nnnnnn
hello world
"""
p10  =re.compile(r'hello.*?world',re.S)
print(p10.findall(key10))

# 11 .分组 (子正则式) 返回元组 返回元组 每一项对应一个子正则式匹配的结果
key11  = r"""hello小明world6677"""
pll =re.compile(r'hello(.*?)world(.*?)77')
print(pll.findall(key11))


"""
正则规则总结：
元字符	说明
.	代表任意字符
|	逻辑或操作符
[ ]	匹配内部的任一字符或子表达式
[^]	对字符集和取非
-	定义一个区间
\	对下一字符取非（通常是普通变特殊，特殊变普通）
*	匹配前面的字符或者子表达式0次或多次
*?	惰性匹配上一个
+	匹配前一个字符或子表达式一次或多次
+?	惰性匹配上一个
?	匹配前一个字符或子表达式0次或1次重复
{n}	匹配前一个字符或子表达式
{m,n}	匹配前一个字符或子表达式至少m次至多n次
{n,}	匹配前一个字符或者子表达式至少n次
{n,}?	前一个的惰性匹配
^	匹配字符串的开头
\A	匹配字符串开头
$	匹配字符串结束
[\b]	退格字符
\c	匹配一个控制字符
\d	匹配任意数字
\D	匹配数字以外的字符
\t	匹配制表符
\w	匹配任意数字字母下划线
\W	不匹配数字字母下划线
"""


# 作业：课下百度re包其他办法 re.match()  re.findall() re.finditer()，跟课上的re.compile  re.search作比较
# 选做 之前一个工作需求 求不是河南移动的
# 了解即可：有人做了一个py包，写代码规则 if else in not，包会把python语法


