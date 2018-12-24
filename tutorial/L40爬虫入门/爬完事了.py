from urllib import request, parse
import re
import os

url = 'https://www.doutula.com/photo/list/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
}
req = request.Request(url,headers=headers)
response = request.urlopen(req)
html = response.read().decode('utf-8')
# print(html)

# 正则匹配
pattern = re.compile('data-original="(.*?)".*?alt="(.*?)"', re.S)
# pattern = re.compile('data-original="(.*?)" alt="(.*?)"')
# 返回存放分组信息的列表
res = re.findall(pattern,html)
# print(res)
# 遍历循环
for info in res:
        src = info[0]
        title = info[1]
        det_pat = re.compile(r'data-original="(.*?)".*?alt="(.*?)"', re.S)
        # print(src)
        path = 'D:\\爬就完事了\\' + title + '.jpg'
        path1 = path
        request.urlretrieve(src, path1)






