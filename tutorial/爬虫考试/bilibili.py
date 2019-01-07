# coding:utf-8
__author__ = 'trc'
import requests
import json
import csv
from CrawlerUtility import ChromeHeaders2Dict


url = 'https://api.bilibili.com/x/web-interface/newlist?callback=jqueryCallback_bili_9144375462500935'
header ="""
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: no-cache
Connection: keep-alive
Cookie: buvid3=E20432F0-4AC7-4BD1-8AB3-88F56417544411417infoc
Host: api.bilibili.com
Pragma: no-cache
Referer: https://www.bilibili.com/v/anime/serial/
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36
"""
headers =ChromeHeaders2Dict(header)
params={
  'rid':33,
  'type':0,
    'pn':1,
    'ps':20,
}

html =requests.get(url,headers=headers,params=params).text
# print(html)
dict = json.loads(html)
#print(dict)
new_list_time=[]
new_list_view=[]
for data in dict['data']['archives']:
    print(data['title'])
    print(data['pic'])
    print(data['ctime'])
    print(data['stat']['view'])


with open('bilibili.csv','a',newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    for i in dict['data']['archives'] :
        writer.writerow([i['title'],i['ctime'],i['stat']['view']])
