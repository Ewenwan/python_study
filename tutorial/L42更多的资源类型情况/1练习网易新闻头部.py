# encoding : utf-8
# import requests
# from lxml import etree
# import re
#
# url ='https://news.163.com/'
# html=requests.get(url).text
# #print(html)
#
# tree =etree.HTML(html)
# header = tree.xpath('//div[@id="js_top_news"]/h2[1]/a/text()')[0]
# header1 =tree.xpath('//*[@id="js_top_news"]/ul[1]/li[1]/a[1]/text()')[0]
# print(f'这个啥鸭子网站的部分头部：{header},{header1}')
import requests
from lxml import etree

url ='http://news.163.com'
resp =requests.get(url)
if resp.status_code != 200:
    raise Exception("请求失败")
html_content=resp.text
# 二进制 resp.content  resp.text自动解码后的字符串
# 偶尔resp.text会解码信息错误、中文乱码。 resp.content.decode(encoding="网页解码类型")

# pattern 模式
pattern1 ='//div[@class="mod_top_news2 and @id="js_top_news"]/h2/a/text()'
pattern2 ='//div[@class="mod_top_news2 and @id="js_top_news"]/ul[@class="top_news_ul"]/li/a/text()'

tree =etree.HTML(html_content)
a=tree.xpath(pattern1)
b=tree.xpath(pattern2)

for i in a :
    print(i)
for j in b:
    print(j)






