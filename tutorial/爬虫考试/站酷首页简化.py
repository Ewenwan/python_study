# coding:utf-8
__author__ = 'trc'
import requests
import threading
import time,os
from lxml import etree
from urllib.request import urlretrieve


url = 'https://www.zcool.com.cn/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

html=requests.get(url,headers=headers).text
tree = etree.HTML(html)
img = tree.xpath('//div[@class="card-img"]//a/img/@src')
print(img)
# 如果没有文件夹就创建文件夹

if not os.path.exists('basedir'):
    os.mkdir('basedir')
# 用枚举确认下标，这样解决for循环问题，，大佬专用
for index,i in enumerate(img):
    # print(index,i)
    src=i.xpath('./@src')[0]       # 这一步错 ， 不知何意
    print(src)


#     urlretrieve(src,'basedir'+f'/{index}.jpg')
# print('保存成功')



