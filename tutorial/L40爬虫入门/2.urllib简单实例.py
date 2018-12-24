# urllib 专门处理http请求响应的内置包
# import urllib  # urllib下面的init——。py没写东西，importurllib  并不会导入其他文件
import urllib.request
# from urllib.request import urlopen
response = urllib.request.urlopen('http://www.baidu.com')# 建议debug看reponse里的东西
# urlopen（url，data={参数1：数值1，参数2：数值2}，timeout=网页响应时间）
print(response)
# 从响应读信息
print(response.code)
html_content=response.read() #socketIO buffReader 模式rb 从响应中读网页信息二进制数据出来。
print(html_content)# 字节类型的网页信息
print(html_content.decode(encoding='utf-8')) #字节解码成字符串


# 网上教程 urllib urllib2,这俩包的区别 urllib3的区别
# python2时代内置处理http的包是urllib，增加改进发布urllib2包，这俩包都内置
# urllib3由第三者开发者发布，语法比较自然，requests基于urllib3
# python3时代吧urllib 和urllib2合并成urllib。。
# 总结：我们现在用的http相关处理包，主要有内置的urllib，第三方requests这俩包，url偏底层，稍微麻烦但原理清楚，requests包封装良好使用简单




