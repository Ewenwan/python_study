import requests
from lxml import etree
from urllib.request import urlretrieve

url = 'http://pic.netbian.com/e/search/result/?searchid=190'
# proxies = {'http': 'http://119.101.112.120:9999'}
# try:
#     html = requests.get('http://www.ivsky.com/tupian/ziranfengguang/', proxies=proxies)
#     print(html.text)
# except Exception as e:
#     print(e)
# else:
#     print('可用')
html = requests.get(url).text.encode('gbk')

# print(html)
lala = etree.HTML(html)
for x in range(1,10):
    img_src = '//*[@id="main"]/div[2]/ul/li[{}]/a/img/@src'.format(x)
    img_name = '//*[@id="main"]/div[2]/ul/li[{}]/a/b/text()'.format(x)
    tu = lala.xpath(img_name)[0]
    hha = lala.xpath(img_src)[0]
    print(tu)
    print(hha)
    tupian = 'http://pic.netbian.com/'+hha

    # tuzhi = tu+'\t'+tupian

    urlretrieve(tupian,filename='D:/美女图片/{}{}.jpg'.format(tu,x))
    # print('正在下载第{}张图片'.format(x))
    if x == 20:
        print('下载完成')
