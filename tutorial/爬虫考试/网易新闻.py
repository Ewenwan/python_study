# coding:utf-8
__author__ = 'trc'

import requests
from lxml.html import fromstring

news_url ='https://news.163.com/'
html =requests.get(news_url).text

xx = fromstring(html)
for i in range(1,8):
    yy = f'//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[3]/div[3]/div[11]/ul/li[{i}]/a/text()'
    paihang = xx.xpath(yy)[0]
    print(f'热点排行的内容是：{paihang}')


