import requests
from lxml import etree
import lxml.html
from urllib.request import urlretrieve
from CrawlerUtility import ChromeHeaders2Dict
import re

url ='https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E9%9B%B6%E9%A3%9F%E5%A4%A7%E7%A4%BC%E5%8C%85&suggest=history_1&_input_charset=utf-8&wq=lingsh&suggest_query=lingsh&source=suggest'
header =""":authority: s.taobao.com
:method: GET
:path: /search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E9%9B%B6%E9%A3%9F%E5%A4%A7%E7%A4%BC%E5%8C%85&suggest=history_1&_input_charset=utf-8&wq=lingsh&suggest_query=lingsh&source=suggest
:scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: no-cache
cookie: thw=cn; cna=1N0XFMcjaCsCAXWgjJmdOyfU; miid=901425892106221713; t=f517682a48bd24b6390e683474b9e521; tracknick=%5Cu54E6%5Cu54E61999%5Cu55EF%5Cu55EF; lgc=%5Cu54E6%5Cu54E61999%5Cu55EF%5Cu55EF; tg=0; enc=z83fIu2tmmCBcteHW1G0VrEpHVV2Ff1lf6lRRnTwaoSG3u3KfzFoaGN2WOqH3bhb0aXJxDl4Vy%2BCXARHmzg66Q%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; uc3=vt3=F8dByRMLl5kwLuPT0MI%3D&id2=UUGrcttDtR2J0g%3D%3D&nk2=piH3d3b3bCPkykKi&lg2=UIHiLt3xD8xYTw%3D%3D; _cc_=V32FPkk%2Fhw%3D%3D; mt=ci=-1_0; v=0; cookie2=11f0bcfd0c533ebb7a021a691d4e1dac; _tb_token_=555eb3387e7eb; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; swfstore=68250; JSESSIONID=F27D15A799AB8E437EEE7BCBE974C9DE; uc1=cookie14=UoTYMb64v3Ff4Q%3D%3D; l=aB5EaxaxyiPwgLCXyMa2jXnYF70jnn5Ppg6C1MayDTEhNtqdkeCXjjno-VwWj_qC5Jcy_K-5F; isg=BDg4VnlJkKO5pPuPzXhfbb1kCeYKCUEapn3FH3KphHMmjdh3GrFsu06vQcWY3VQD
pragma: no-cache
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"""
headers = ChromeHeaders2Dict(header)
html = requests.get(url,headers=headers).text
# print(html)
aa =re.compile('"raw_title":"(.*?)","pic_url":')
bb = re.findall(aa,html)
cc =re.compile('"pic_url":"(.*?)","detail_url":')
dd =re.findall(cc,html)
x = 1
for i in range(1,len(dd)):
    tupian =dd[i]
    tupian1 ='http:'+tupian
    title=bb[i]


    print(tupian1,title)
    urlretrieve(tupian1,filename=f'D:/淘宝零食大礼包/{x}.jpg')
    x+=1
