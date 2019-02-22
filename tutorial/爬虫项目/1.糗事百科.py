# coding:utf-8
__author__ = 'trc'
import requests,sqlite3,re,pymysql

class ProcessDataTool(object):
    """
    工具类：工具类中一般不写——init——初始化属性，只封装工具方法对数据进行操作。工具类中的方法一般是以工具类居多
    """
    @classmethod
    def process_data(cls,data_tuple):
        """
        对原始数据处理完成，返回一个新的元组
        :param data_tuple:
        :return:
        """
        # print(data_tuple)
        p1 = re.compile(r'\n',re.S)
        p2 = re.compile(r'<br/>',re.S)

        nickname = data_tuple[0]
        # 利用正则表达式sub ，从nickname中匹配\n，并将其替换成''空字符串
        nickname = re.sub(p1,'',nickname)

        content = data_tuple[2]
        content = re.sub(p1,'',content)
        content = re.sub(p2,'',content)

        return nickname , data_tuple[1] ,content,data_tuple[3],data_tuple[4]
def Mysql(data):
    print(data)
    connect = pymysql.connect(user='root', password='trc', host='127.0.0.1', db='pachong')
    cursor = connect.cursor()
    # cursor.execute("""
    #         CREATE TABLE qsbk(id INT PRIMARY KEY AUTO_INCREMENT,
    #         nick_name VARCHAR (20),
    #         level int ,
    #         content varchar (1000),
    #         smell_count int ,
    #         comment_count int
    #         );
    #     """)
    insert_sql = 'insert into qsbk(nick_name,level,content,smell_count,comment_count) values (%s,%s,%s,%s,%s)'
    cursor.execute(insert_sql, data)
    connect.commit()
    connect.close()
    cursor.close()
class DBTool(object):
    conn = cursor = None

    @classmethod
    def conn_cursor(cls):
        cls.conn = sqlite3.connect('qsbk.db')
        cls.cursor = cls.conn.cursor()

    @classmethod
    def insert_data(cls, data):
        cls.cursor.execute("""
        CREATE TABLE qsbk(id INT PRIMARY KEY,
        nick_name VARCHAR (20),
        level int ,
        content varchar (1000),
        smell_count int ,
        comment_count int
        )""")
        insert_sql = 'INSERT INTO qsbk(nick_name, level, content, smell_count, comment_count) VALUES (?,?,?,?,?)'
        cls.cursor.execute(insert_sql,data)
        cls.conn.commit()

    @classmethod
    def close_connect(cls):
        cls.cursor.close()
        cls.conn.close()
class QSBKSpider(object):
    """
    爬虫类
    """
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    def get_list_page(self,page_num):
        """
        获取列表页源代码
        :param page_num:
        :return:
        """
        try:
            url =f'https://www.qiushibaike.com/hot/page/{page_num}/'
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                # 返回网页源代码字符串 交给下一个函数解析
                return response.text
            else:
                # 202:表示对方服务器已经成功接收了get请求，但是并没有给予响应  如果多次尝试都是202 说明收到爬虫的限制了
                print(f'状态码异常{response.status_code},url地址:{url}')
                return None
        except Exception as  e:
            print(f'当前url:{url}请求异常，异常的原因:{e}')
            return None
    def parse_list_page(self,html):
        """
        解析列表页源代码
        :param html:
        :return:
        """
        pattern = re.compile(r'<div class="article.*?<div class="author clearfix.*?<h2>(.*?)</h2>.*?<div class="articleGender.*?">(.*?)</div>.*?<span>(.*?)</span>.*?<span class="stats-vote"><i class="number">(.*?)</i> 好笑</span>.*?<span class="stats-comments">.*?<i class="number">(.*?)</i>',re.S)
        datas = re.findall(pattern,html)
        for data_tuple in datas:
            # 将原始数据交给工具类进行数据的整理 nick_name,level,content,smail_count,comment_count
            new_data_tuple = ProcessDataTool.process_data(data_tuple)
            Mysql(new_data_tuple)
if __name__ == '__main__':
    spiders = QSBKSpider()
    html = spiders.get_list_page(1)
    if html:
        spiders.parse_list_page(html)
    else:
        pass



