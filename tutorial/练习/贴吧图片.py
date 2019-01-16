# coding:utf-8
__author__ = 'trc'

from lxml.html import fromstring
import requests
import re
from CrawlerUtility import ChromeHeaders2Dict
url = "http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E8%83%A1%E6%AD%8C"

html = requests.get(url).text
print(html)
a = re.compile('"middleURL":"(.*)",')
b = re.compile('')
c = re.compile('')
aa = re.findall('.*?"thumbURL":"(.*?)".*?',html,re.S)
print(aa)


