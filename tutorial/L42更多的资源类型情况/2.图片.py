# coding:utf-8
# 情况2：纯静态网页获取图片
# 解决2方案：requests包会接收相应的二进制数据，取出后写入到本地。
# 分析网页，比纯静态文本麻烦一点，图片往往通过src标签或a标签引入到网页，第一步先分析获取图片在网页上的url资源地址，第二步请求静态资源地址获取图片二进制信息。

# 需求：爬取天堂图片网图片
import requests
from lxml import etree
from urllib.request import urlretrieve
import os

url = 'http://www.ivsky.com/tupian/yueliang_v49681/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
}
html_content = requests.get(url, headers=headers).text

# 获取图片src地址列表
for x in range(0,5):
    pattern_img_src = '//ul[@class="pli"]/li/div/a/img/@src'

    html_dom = etree.HTML(html_content)
    img_src_list = html_dom.xpath(pattern_img_src)[x]
    print(img_src_list)

    urlretrieve(img_src_list,filename='D:/Crawl_pictures/text{}.jpg'.format(x))
    print('下载{}'.format(x))




# 请求单张图片
pattern_img_src = '//ul[@class="pli"]/li/div/a/img/@src'
html_dom = etree.HTML(html_content)
img_src_list = html_dom.xpath(pattern_img_src)

for index,img_src_url in enumerate(img_src_list):
    # img_src_url = 'http://img.ivsky.com/img/tupian/t/201806/15/yueliang.jpg'
    resp = requests.get(img_src_url, timeout=10)
    if resp.status_code !=200:
        raise Exception("图片请求失败")
    img_bytes = resp.content
    print(img_bytes)
    # 读写信息到本地
    # with open(f'{index}.jpg','wb') as file:
        # file.write(img_bytes)


