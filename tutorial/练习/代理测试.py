# coding:utf-8
__author__ = 'ym'
import requests
import json
import random
import lxml.html
from CrawlerUtility import ChromeHeaders2Dict
import os
import re


class Tiantangspider:

    def get_proxy(self):
        """获取代理"""
        pro_url = 'http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=fc1a46b572d54ca0a12f375eceb3b5e8&count=20&expiryDate=0&format=1&newLine=2'
        # url = 'http://www.baidu.com/s?wd=ip'
        pro = requests.get(pro_url).text
        pro_dict = json.loads(pro)
        proxy_list = pro_dict['msg']
        proxy = random.choice(proxy_list)
        ip = proxy['ip']+':'+proxy['port']
        proxies = {
            'http': ip
        }
        return proxies

    def img_spider(self):
        """获取天堂图片自然风光第一页相册和名字
            :return:相册url列表和相册名字列表
        """
        headers = """Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
Cache-Control: no-cache
Connection: keep-alive
Cookie: Hm_lvt_862071acf8e9faf43a13fd4ea795ff8c=1545642322,1545708670; _pk_ref.5.c0e8=%5B%22%22%2C%22%22%2C1545708670%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D55f1Q55nPFz9xKB4xVTCYXg7lyTFwo5S5shGAaSpPu3%26wd%3D%26eqid%3Dcd82ec7c0001ed55000000035c21a43d%22%5D; _pk_ses.5.c0e8=*; statistics_clientid=me; arccount49681=c; _pk_id.5.c0e8=484a0c53c948d866.1545642322.2.1545710436.1545708670.; Hm_lpvt_862071acf8e9faf43a13fd4ea795ff8c=1545710436
Host: www.ivsky.com
Pragma: no-cache
Referer: http://www.ivsky.com/tupian/yueliang_v49681/
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"""
        header = ChromeHeaders2Dict(headers)
        url = 'http://www.ivsky.com/tupian/ziranfengguang/'
        html_info = requests.get(url, headers=header).text
        selector = lxml.html.fromstring(html_info)
        img_url_list = selector.xpath('/html/body/div[3]/div[2]/ul/li/div/a/@href')
        img_url_list_title = selector.xpath('/html/body/div[3]/div[2]/ul/li/p/a/text()')
        img_url_lista = []
        #print(img_url_list)
        #print(img_url_list_title)
        for img_url in img_url_list:
            str1 = 'http://www.ivsky.com'
            img_u  = str1 + img_url
            img_url_lista.append(img_u)
        return img_url_lista, img_url_list_title

    def get_img(self):
        """获取相册页面图片url
            :return:图片列表和相册名字列表
        """
        header = """Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
Cache-Control: no-cache
Connection: keep-alive
Cookie: Hm_lvt_862071acf8e9faf43a13fd4ea795ff8c=1545642322,1545708670; _pk_ref.5.c0e8=%5B%22%22%2C%22%22%2C1545708670%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D55f1Q55nPFz9xKB4xVTCYXg7lyTFwo5S5shGAaSpPu3%26wd%3D%26eqid%3Dcd82ec7c0001ed55000000035c21a43d%22%5D; _pk_ses.5.c0e8=*; statistics_clientid=me; arccount49681=c; arccount49966=c; BDTUJIAID=2d237a99632fbae22e2cf1cd04a0b617; Hm_lpvt_862071acf8e9faf43a13fd4ea795ff8c=1545711508; _pk_id.5.c0e8=484a0c53c948d866.1545642322.2.1545711508.1545708670.
Host: www.ivsky.com
Pragma: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"""
        headers = ChromeHeaders2Dict(header)
        img_url_list_b = []
        img_url_lista, img_url_list_title = self.img_spider()
        for img_url in img_url_lista:
            html_info = requests.get(img_url, headers=headers).text
            selector = lxml.html.fromstring(html_info)
            img_url_list = selector.xpath('/html/body/div[3]/div[4]/ul/li/div/a/img/@src')
            #print(img_url_list)
            img_url_list_b.append(img_url_list)
        return img_url_list_b, img_url_list_title

    def save(self):
        """保存图片到本地"""
        img_url_list_b, img_url_list_title = self.get_img()
        for i in range(len(img_url_list_title)):
            num = 1
            print(img_url_list_b)
            for ii in img_url_list_b[i]:
                url = re.sub('tupian/(.*?)/', 'tupian/pre/', ii)  # 替换成大图片url
                print(url)
                html_content = requests.get(url).content
                # print(html_content)
                if os.path.exists(f'D:/天堂图片1/{img_url_list_title[i]}') == True:
                    os.chdir(f'D:/天堂图片1/{img_url_list_title[i]}')
                else:
                    os.makedirs(f'D:/天堂图片1/{img_url_list_title[i]}')
                    os.chdir(f'D:/天堂图片1/{img_url_list_title[i]}')
                with open(f'{num}.jpg', 'wb') as file:
                        file.write(html_content)
                # print(f'正在保存{img_url_list_title[i]}, {num}.jpg')
                num += 1

if __name__ == '__main__':
    x = Tiantangspider()
    x.save()



