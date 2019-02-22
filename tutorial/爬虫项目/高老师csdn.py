# 关键点：
# 1. 首次展示的数据是通过网页源代码返回的数据，后面下拉加载的时候通过json接口返回的数据。问题：json接口如何得知网页源代码的最后一条数据？
# 2. 上一次json接口返回的数据和下一次json接口返回的数据是如何关联的？

import requests, re, json

class CSDNSpider(object):
    def __init__(self):
        # 首次刷新页面，其中20/21数据是通过html源代码返回的，剩余的数据才是通过json接口返回的。所以不能直接去请求api接口。
        self.start_url = 'https://www.csdn.net/nav/career'
        self.json_api = 'https://www.csdn.net/api/articles?type=more&category=career&shown_offset={}'
        self.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}

    def get_list(self):
        """
        负责从源代码中提取shown-offset属性的值，并将21/20条数据利用正则提取出来。
        :return:
        """
        response = requests.get(url=self.start_url, headers=self.headers)
        if response.status_code == 200:
            shown_offset = re.search(re.compile(r'<ul.*?id="feedlist_id" shown-offset="(.*?)">', re.S), response.text).group(1)
            print(shown_offset)
            datas = re.findall(re.compile(r'<div class="title">.*?<a.*?>(.*?)</a>.*?<div class="summary oneline">(.*?)</div>.*?<dd class="name">.*?<a.*?>(.*?)</a>.*?<dd class="time">(.*?)</dd>.*?<a.*?>(.*?)</a>.*?<a.*?>(.*?)</a>', re.S), response.text)
            for data in datas:
                char = re.compile(r'\n|\r|\t| ')
                title = re.sub(char, '', data[0])
                info = re.sub(char, '', data[1])
                author = re.sub(char, '', data[2])
                pub_date = re.sub(char, '', data[3])
                read_num = re.sub(char, '', data[4])
                comment_num = re.sub(char, '', data[5])

                if '<spanclass="num">' in read_num:
                    # 有阅读量
                    read_num = re.search(re.compile(r'<spanclass="num">(.*?)</span>', re.S), read_num).group(1)
                else:
                    read_num = '0'
                if '<spanclass="num">' in comment_num:
                    # 有评论量
                    comment_num = re.search(re.compile(r'<spanclass="num">(.*?)</span>', re.S), comment_num).group(1)
                else:
                    comment_num = '0'
                print(read_num, '---', comment_num)
            # 将这个起始的shown-offset的值作为json接口的参数发起第一次接口请求。
            self.parse_json(shown_offset)
        else:
            print('请求首页状态码异常：{}'.format(response.status_code))

    def parse_json(self, shown_offset):
        """
        负责请求json接口，并对json解析，从而提取数据。
        :param shown_offset:
        :return:
        """
        url = self.json_api.format(shown_offset)
        response = requests.get(url=url, headers=self.headers)
        if response.status_code == 200:
            json_dict = json.loads(response.text)
            articles = json_dict['articles']
            print(len(articles))
            offset = json_dict['shown_offset']
            self.parse_json(offset)

if __name__ == '__main__':
    csdn = CSDNSpider()
    csdn.get_list()
