# coding:utf-8
__author__ = 'trc'
import requests,sqlite3,json,re,pymysql

def Mysql(data):
    print(data)
    connect = pymysql.connect(user='root', password='trc', host='127.0.0.1', db='pachong')
    cursor = connect.cursor()
    insert_sql = 'insert into 51jobs(zw_title,company_name,zw_position,salary,pub_date,region,welfare,detail) values (%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(insert_sql,data)
    connect.commit()
    connect.close()
    cursor.close()
class ProcessDataTool(object):
    """
    数据处理的工具类：工具类中一般不写__init__初始化属性，只封装工具方法对数据进行操作。工具类中的方法一般是以类方法居多。
    """
    @classmethod
    def process_data(cls, data_tuple):
        """
        对原始的元组数据处理完成，返回一个新的元组
        :param data_tuple:
        :return:
        """
        # print(data_tuple)
        # 经过输出，发现用户昵称和段子内容需要处理特殊字符，将\n和<br/>从原始字符串中删除。
        p1 = re.compile(r'\n|\r|\t|&nbsp;', re.S)
        # <div>  </div> <a> </a> <p> </p>
        p2 = re.compile(r'<.*?>', re.S)
        yq_abstract = re.sub(p1, '', data_tuple[0])
        yq_abstract = re.sub(p2, '', yq_abstract)

        fl_abstract = re.sub(p1, '', data_tuple[1])
        fl_abstract = re.sub(p2, '', fl_abstract)

        yq_content = re.sub(p1, '', data_tuple[2])
        yq_content = re.sub(p2, '', yq_content)

        return yq_abstract, fl_abstract, yq_content
class Job51Spider(object):
    def __init__(self):
        self.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}
        self.code_dict={}
    def parse_city_code(self):
        """
        获取城市对应的编码，北京：010000
        :return:
        """
        try:
            response = requests.get('https://js.51jobcdn.com/in/js/2016/layer/area_array_c.js?20180319')
            if response.status_code == 200:
                # 目的是将{}和{}中的所有内容都提取出来，此时{}就是一个普通的字符，但是{}在正则表达式中表示匹配字符的个数\d{4}、\w{3}，所以在正则表达试中，如果想将{} （） + - 等特殊字符转换为一个普通的字符，此时需要\{\}
                pattern = re.compile(r'var area=(.*?);',re.S)
                # .group(1): 表示提取正则表达式中第一个分组（.*?）中的数据
                json_str = re.search(pattern,response.text).group(1)
                json_dict = json.loads(json_str)
                for key,value in json_dict.items():
                    self.code_dict[value] = key
            else:
                print('城市编码请求异常：{}'.format(response.status_code))
        except Exception as e:
            print('城市编码请求异常{}'.format(e))
    def get_list_page(self,):
        """
        请求列表页 ，获取源代码，交给下一个函数用正则对数据的提取
        :return:
        """
        citys = ['北京', '上海', '广州']
        code_str = ''
        for city in citys:
            code = self.code_dict[city]
            if city != city[-1]:
                code_str += code
                code_str += '%252c'
            else:
                code_str += code
        self.url = 'https://search.51job.com/list/' + code_str + ',000000,0000,00,9,99,python,2,{}.html'
    def parse_list_page(self,list_num):
        """
        解析列表页的职位信息
        :param list_html: 返回源代码
        :return: 这里只能得到列表页，无法得到详细信息
        """
        print('正在打印第{}'.format(list_num))
        list_url = self.url.format(list_num)
        try:
            response = requests.get(url=list_url,headers=self.headers)
            if response.status_code == 200:
                pattern = re.compile(r'<div class="el">.*?<a.*?title="(.*?)" href="(.*?)".*?<a.*?title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>', re.S)
                response.encoding = 'gbk'
                ssddf = response.text
                list_html = re.findall(pattern,ssddf)
                # del json_str[0]
                return list_html
            else:
                print('城市编码请求异常：{}'.format(response.status_code))
                return None
        except Exception as e:
            print('城市编码请求异常{}'.format(e))
            return None
    def get_detail_page(self, detail_url):
        """
        请求详情页url，得到详情页的网页源代码
        :return: 交给下一个函数进行详情页数据的提取
        """
        try:
            response = requests.get(url=detail_url, headers=self.headers)
            if response.status_code == 200:
                return response.content.decode('gbk')
            else:
                print('详情页状态码异常：{}'.format(response.status_code))
                return None
        except Exception as e:
            print('详情页请求失败：{}'.format(e))
            return None
    def parse_detail_page(self, detail_html, detail_url):
        """
        解析详情页数据，和列表页的数据一起存入数据库即可。
        :param detail_html:
        :return:
        """
        # 由于详情页的页面结构可能存在不一样的情况，所以需要通过详情页的url地址来判断具体采用什么样的正则表达式。
        if 'jobs.51job.com' in detail_url:
            pattern = re.compile(
                r'<div class="cn">.*?<h1 title="(.*?)">.*?<strong>(.*?)</strong>.*?<a.*?title="(.*?)".*?<p class="msg ltype" title="(.*?)".*?<div class="t1">(.*?)</div>.*?<div class="tBorderTop_box">.*?<div class="bmsg.*?">(.*?)</div>',
                re.S)
            detail_data = re.findall(pattern, detail_html)
            if detail_data:
                return detail_data[0]
            else:
                print('列表为空')
                return None
        elif '51rz.51job.com' in detail_url:
            print(detail_url)
            return None
        else:
            print(detail_url)
            return None
if __name__ ==  '__main__':
    sp = Job51Spider()
    sp.parse_city_code()
    sp.get_list_page()
    for x in range(1,100):
        list_html = sp.parse_list_page(x)
        if list_html:
            list_html = sp.parse_list_page(x)
            for zw_title, detail_url, company_name, zw_position, salary, pub_date in list_html:
                detail_html = sp.get_detail_page(detail_url)
                detail_data = sp.parse_detail_page(detail_html, detail_url)
                if detail_data:
                    new_data = ProcessDataTool.process_data((detail_data[3], detail_data[4], detail_data[5]))
                    data = (
                    zw_title, company_name, zw_position, salary, pub_date, new_data[0], new_data[1],new_data[2])
                    Mysql(data)





