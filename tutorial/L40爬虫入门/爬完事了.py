import requests
import re
from urllib.request import urlretrieve

url = 'https://www.doutula.com/photo/list/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
}
html = requests.get(url,headers=headers).text
# print(html)

# 正则匹配
#pattern = re.compile('data-original="(.*?)".*?alt="(.*?)"', re.S)
pattern = re.compile('data-original="(.*?)" alt="(.*?)"')
# 返回存放分组信息的列表
res = re.findall(pattern,html)
print(res)
# 遍历循环
for info in res:
        src = info[0]
        title = info[1]
        print(src)
        print(title)
        path = 'D:/爬就完事了1/' + title + '.jpg'
        path1 = path
        path2=path1
        path3=path2
        path4 =path3
        urlretrieve(src, path4)






