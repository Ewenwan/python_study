import requests
from lxml.html import fromstring
from urllib.request import urlretrieve

url='https://www.vcg.com/creative'
html = requests.get(url).text
# print(html)

tree = fromstring(html)

# for i in range(1,10):
img_src='//*[@id="root"]/main/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[1]/a/div/div/@style'
src = tree.xpath(img_src)
print(src)

    # urlretrieve(img_src,filename='D:/李大米一号/{}.jpg'.format(name))
