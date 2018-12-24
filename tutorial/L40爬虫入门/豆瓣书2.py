#糗事百科热点文章爬取
#分析： 请求 url https://www.qiushibaike.com/hot/page1/ 要抓取div class='article' urllib或requests
# coding:utf-8
import requests
import urllib.request
from fake_useragent import UserAgent
import random
import re
base_url = 'https://book.douban.com/?qq-pf-to=pcqq.group'
url = base_url  + '1' + '/'

print(base_url)

ua = UserAgent()

headers={
     'UserAgent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
}

response = requests.get(base_url,headers=headers).text
pattern = re.compile(r'<div class="d-wname".*?<a.*?>(.*?)</a>.*?',re.S) #re.S匹配包括换行后
results = re.findall(pattern,response)
print(results)
# for row in results:
#      print(row)

# pattern2 =re.compile(r'<div class="gird-16-8 clearfix">.*?<h2>(.*?)</h2>',re.S)
# results2 = re.findall(pattern2,html_content)
# print(results2)
