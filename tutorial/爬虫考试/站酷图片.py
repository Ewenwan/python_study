# coding:utf-8
__author__ = 'trc'
import requests
from lxml.html import fromstring
from urllib.request import urlretrieve

url ='https://www.zcool.com.cn/work/ZMzI2MTMwNDQ=.html'

html = requests.get(url).text
lala = fromstring(html)
for i in range(1,11):
    yy=f'//*[@id="body"]/main/div[2]/div[2]/div[1]/div/div[3]/div[{i}]/img/@src'
    tupian = lala.xpath(yy)[0]
    print(tupian)
    print(f'正在保存第{i}张图片')
    urlretrieve(tupian, filename=f'D:/站酷图片/站酷图片{i}.jpg')
    if i == 10:
        print('保存完成')
