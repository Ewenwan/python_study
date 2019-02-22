# coding: utf8
import json, requests, re

# JSON数据的分析：
# 1. 一般一个网站如果是通过下拉加载/加载更多来获取和展示数据的，90%的情况都是有json接口的，优先查找json接口；
# 2. 如果一个网站是有分页的，这种网站可能是静态网站(网页源代码中就有数据)，也有可能是动态网站(网页源代码中没有数据，是一堆的<script>标签)，如果是静态网站直接使用re、xpath等解析网页源代码即可；如果是动态网站，先分析是不是有json接口；如果没有json接口，再去源代码中查看以下json数据是否包含在<script>标签中；如果以上都无法获取数据，再使用selenium动态加载js代码，获取完整的网页源代码并解析；

class ZLSpider(object):
    def __init__(self):
        self.url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=538&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&_v=0.95260331&x-zp-page-request-id=595f636d6e5c4ab9853f3217b841582d-1550714982546-78357&start={}'
        # 声明变量，用于记录接口中start偏移量的值(0, 90, 180.....)
        self.offset = 0

    def get_json_str(self):
        """
        请求智联json接口，并返回json字符串
        :return:
        """
        url = self.url.format(self.offset)
        response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'})
        if response.status_code == 200:
            return response.text
        else:
            print('接口请求状态码异常：{}'.format(response.status_code))
            return None

    def parse_json(self, json_str):
        """
        解析列表页的json接口
        :param json_str:
        :return:
        """
        json_dict = json.loads(json_str)
        results = json_dict.get('data').get('results')
        if results:
            for zhiwei_dict in results:
                # 福利待遇
                # ['1', '2']: ';'.join()它会将列表中的每一个元素，使用;拼接成一个字符串 '1;2' '12' ''.join()
                welfare = ';'.join(zhiwei_dict['welfare'])
                # 薪资待遇
                salary = zhiwei_dict['salary']
                # 职位名称
                jobName = zhiwei_dict['jobName']
                # 职位详情
                detail_url = zhiwei_dict['positionURL']
                content = self.get_detail(detail_url)
                print(welfare, salary, jobName, content)
            # 继续请求后续的数据
            self.offset += 90
            j = self.get_json_str()
            self.parse_json(j)
        else:
            print('已经没有职位了')

    def get_detail(self, detail_url):
        """
        请求并解析详情页的数据
        :param detail_url:
        :return:
        """
        html = requests.get(detail_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}).text
        content = re.search(re.compile(r'<div class="pos-ul".*?>(.*?)</div>', re.S), html).group(1)
        content = re.sub(re.compile(r'<.*?>', re.S), '', content)
        return content

if __name__ == '__main__':
    zl = ZLSpider()
    j_s = zl.get_json_str()
    zl.parse_json(j_s)