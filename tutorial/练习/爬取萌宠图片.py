import requests
from lxml import etree
from urllib.request import urlretrieve



url = 'http://pic.netbian.com/e/search/result/?searchid=8336'
# proxies = {'http': 'http://119.101.112.120:9999'}
html = requests.get(url).text

print(html)
lala = etree.HTML(html)
for x in range(1,10):
    img_rsc = '//*[@id="main"]/div[2]/ul/li[{}]/a/img/@src'.format(x)
    img_name = '//*[@id="main"]/div[2]/ul/li[{}]/a/b/text()'.format(x)
    tu = lala.xpath(img_name)[0]
    hha = lala.xpath(img_rsc)[0]
    print(tu)
    print(hha)
    tupian = 'http://pic.netbian.com/'+hha

    # tuzhi = tu+'\t'+tupian

    urlretrieve(tupian,filename='D:/萌宠图片/{}{}.jpg'.format(tu,x))
    print('正在下载第{}张图片'.format(x))
    if x == 10:
        print('下载完成')
