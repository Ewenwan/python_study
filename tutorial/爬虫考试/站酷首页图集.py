# coding:utf-8
__author__ = 'trc'
import requests
import threading
import time, os
from lxml import etree
from urllib.request import urlretrieve


class ZkDownload(object):
    def __init__(self):
        self.url='https://www.zcool.com.cn/'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        self.base_dir="D:/zkImgs/"
        self.basedir="basedir"
        self.html = ''
        self.count=0

    #获取html
    def get_html(self,url):
            """引入代理ip"""
            time.sleep(5)
            try:
                response = requests.get(url, headers=self.headers)
            except Exception as e:
                print('正在连接请稍后.....')
            else:
                self.html = response.text
                response.close()

    #保存首页列表图片
    def keep_listimg(self):
        tree = etree.HTML(self.html)
        imgs = tree.xpath('//div[@class="card-img"]//a/img')
        #如果没有就创建文件夹
        if not os.path.exists(self.basedir):
            os.mkdir(self.basedir)
        #取出首页图片链接 进行保存
        for index, i in enumerate(imgs):
            src = i.xpath('./@src')[0]
            urlretrieve(src, self.basedir+f'/{index}.jpg')
        print('保存成功')

    #解析列表页，提取图片详情
    def parse_list(self):
        tree = etree.HTML(self.html)
        content = tree.xpath('//div[@class="card-info"]//a')
        content.pop()
        for c in content:
            self.count+=1
            title = c.xpath('./@title')[0].replace('|','')
            hrefs = c.xpath('./@href')[0]
            print("正在爬取:{},第{}图集".format(title,self.count))
            self.parse_detail(title,hrefs)
            #print(title,hrefs)
            #// div[ @class ="reveal-work-wrap"] // img

    #解析详情图片页
    def parse_detail(self,title,hrefs):
        self.get_html(url=hrefs)
        #创建文件夹
        if not os.path.exists(self.base_dir+title):
            os.makedirs(self.base_dir+title)
        #解析详情页图片链接
        etr = etree.HTML(self.html)
        img_hrefs = etr.xpath('//div[@class="reveal-work-wrap"]//img')
        for img in img_hrefs:
            links = img.xpath('./@src')[0]
            name = links.split('/')[-1]
            #拼接完整的图片存放路径
            print("图片详情链接和地址"+self.base_dir+"/"+name)
            #启用多线程下载
            t = threading.Thread(target=self.dowmload_img,args=(links,self.base_dir+title+"/"+name))
            t.start()

    def dowmload_img(self,links,name):
        b_img = requests.get(links, headers=self.headers).content
        with open(name, 'wb') as f:
            f.write(b_img)

    #启动函数
    def run(self):
        time.sleep(5)
        for i in range(1,2):
            self.get_html("https://www.zcool.com.cn/?p="+str(i)+"tab_anchor")
            self.parse_list()


if __name__=='__main__':
    #https: // www.zcool.com.cn /?p = 2  # tab_anchor
    zk = ZkDownload()
    zk.run()