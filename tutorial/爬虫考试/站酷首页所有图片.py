# coding:utf-8
__author__ = 'trc'
import requests
from lxml.html import fromstring
from urllib.request import urlretrieve

url ='https://www.zcool.com.cn/'

html = requests.get(url).text
lala = fromstring(html)
for i in range(1,21):
    src=f'//*[@id="body"]/main/div[3]/div/div[{i}]/div[1]/a/img/@src'
    biaoti =f'//*[@id="body"]/main/div[3]/div/div[{i}]/div[1]/a/img/@title'
    tupian = lala.xpath(src)[0]
    title  = lala.xpath(biaoti)[0]
    print(tupian,title)
    print(f'正在保存第{i}张图片')
    urlretrieve(tupian, filename=f'D:/站酷首页图片/站酷图片{i}.jpg')
    if i == 20:
        print('保存完成')