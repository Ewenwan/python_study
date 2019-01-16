# coding:utf-8
__author__ = 'trc'
import  re
import requests
import time
from lxml import etree

word = input('请输入你要搜索的图片：')

#百度复制搜索栏： ‘http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1547206670591_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%83%A1%E6%AD%8C’

# 'http://image.baidu.com/search/index?tn=baiduimage&ie=utf-8&word=胡歌' 简化word必须有

url = 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1547206670591_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=' + word + ''    # 拼接的url

result = requests.get(url)        # requests 解析
if result.status_code == 200:     # 如果响应等于  打印html
    html=result.text
    print(html)# 不用管编码问题， encoding='utf-8'就行，没必要

#  先用正则  ，正则万物都可以取   百度图片网址不可以用xpath解析，因为是动态网站，用java加载的
    html_url=re.findall('"objURL":"(.*?)",',html,re.S)
    print(html_url)
    # i= 1
    # print('找到:' + word + '的图片，正在下载...')    # 拼接
    # for x in html_url:                    # 循环多个
    #     print('正在下载第'+ str(i) + '张图片')
    #     pic = requests.get(x)
    #     dir = '../'+ word +'_' + str(i) + '.jpg'
    #     hg = open(dir,'wb')               # 保存本地
    #     hg.write(pic.content)
    #     hg.close()
    #     i +=1
    #     time.sleep(3.5)



