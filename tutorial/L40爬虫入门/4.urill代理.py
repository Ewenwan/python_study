# urllib代理实例
# 为了防止同一个ip频繁访问服务器被封锁，需要不断变化ip通过别人电脑的代理访问服务器。

"""
 从哪找代理？
1.ip代理平台 http://www.xicidaili.com.cn
免费的不太稳定有些不可用。付费的稳定。
2.网友搜集的ip代理爬取值
"""

import urllib.request
# 设置操作代理器    ProxyHandler 前处理程序
proxy=urllib.request.ProxyHandler({'http':'http://124.231.50.56:8118'})
# 构建新的请求器 覆盖默认opener proxy代理服务器 response反应
opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
response=urllib.request.urlopen('http://www.zznews.gov.cn/news/xinwen/zzsz/')
html_content=response.read().decode('utf-8')
# 返回结果中查找“本机ip”看是否变成代理ip
print(html_content)

"""
可能出现的错误
1. 长时间未响应。urllib.error.YRLError: <urlopen error[WinErroe 10060]> 由于连接方在一段时间后没有正确的答复或连接的主机没有反应，连接尝试失败。>
2. 对方服务器拒绝连接。    connectionResetError远程主机关闭了一个现有连接。
解决， 换一个或购买付费接口。
"""
"""
代理池：一个两个ip不都用，需要列表，手动添加代理麻烦。
解决方案，专门写一个爬ip代理网站免费信息的爬虫，把爬下来的代理信息不断做测试，把接成功的放到数据库中。当我们写爬虫是，从已爬去的ip代理池中获取代理ip
"""

