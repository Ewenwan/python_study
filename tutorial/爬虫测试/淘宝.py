# coding:utf-8
__author__ = 'trc'

import requests
import json
from lxml.html import fromstring

url = 'https://shop111126855.taobao.com/?spm=a217f.8051907.1238938.2.45443308jZms4B'

html = requests.get(url).text
#print(html)

a=fromstring(html)
b='//*[@id="shop21262490999"]/div/div/span/div/div/map/area[1]/@href'
y=a.xpath(b)
print(y)


