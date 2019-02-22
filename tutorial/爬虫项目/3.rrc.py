# coding:utf-8
__author__ = 'trc'
from  fake_useragent import UserAgent
from  multiprocessing import Pool
import requests,sqlite3,re,pymysql

class RRCSpider(object):
    def __init__(self):
        self.url = 'https://www.renrenche.com/zz/benchi/p{}/'
        self.ua = UserAgent(use_cache_server=False)


    def get_list_page(self,page_num):
        """
        得到请求页
        :param page_num:
        :return:
        """
        print('正在请求第{}页'.format(page_num))
        # 开始利用self.url拼接page_num，构造完整的url地址。
        list_url = self.url.format(page_num)
        try:
            response = requests.get(url=list_url,headers = {'user-agent':self.ua.chrome})
            if response.status_code == 200:
                return response.text
            else:
                print('列表页状态码异常：{}'.format(response.status_code))
                return None
        except Exception as e:
            print('列表页请求失败：{}'.format(e))
            return None

    def parse_list_page(self,list_html):
        """

        :param list_html:
        :return:
        """
        patt = re.compile(r'',re.S)
        detail_urls = re.findall(patt,list_html)
        return  detail_urls
    def get_detail_page(self,detail_url):
        """
        :param detail_url:
        :return:
        """
    def parse_detail_page(self,detail_html):
        """

        :param detail_html:
        :return:
    """
    def start(self, num):
        list_html = self.get_list_page(num)
        if list_html:
            urls = self.parse_list_page(list_html)
            # print(urls)
            for detail_url in urls:
                detail_html = self.get_detail_page(detail_url)
                if detail_html:
                    self.parse_detail_page(detail_html, detail_url)

if __name__ =='__main__':
    obj = RRCSpider()
    pool = Pool(3)
    pool.map(obj.start,[x for x in range(1,51)])
    # for x in range(1,50):
    #     list_html = obj.get_list_page(x)
    #     if list_html:
    #         urls = list_data = obj.parse_list_page(list_html)
    #         print(urls)
    #         for detail_url in urls:
    #             obj.get_detail_page(detail_url)

