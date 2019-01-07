# coding:utf-8
__author__ = 'ym'
import json
import pymysql
import jieba
import pygal
from wordcloud import WordCloud


class XmComment(object):
    def __init__(self):
        self.conn = pymysql.connect(user='root', password='123', db='test')
        self.cursor = self.conn.cursor()

    def get_dict(self, num):
        """获取评论数据"""
        data = json.load(open(f'tb_comments_{num}.json', encoding='utf-8'))
        comment_list = data['rateDetail']['rateList']
        comment_info = []
        for i in comment_list:  # 构造评论数据字典
            comment = i['rateContent']
            rateDate = i['rateDate']
            id = int(i['id'])
            auctionSku = i['auctionSku']
            if i['appendComment'] == None:  # 判断用户是否追加评论
                appendComment = '用户没有追加评论'
            else:
                appendComment = i['appendComment']['content']
            # 添加到数据列表中返回
            comment_info.append({'评论': comment, '评论时间': rateDate, 'comment_id': id, '商品类型': auctionSku, '追加评论': appendComment})
        return comment_info  # 返回评论数据列表

    def save_db(self, comment_info):
        """保存到数据库"""
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS xmcomment
        (
        id INT PRIMARY KEY AUTO_INCREMENT,
        comment_id BIGINT ,
        comment VARCHAR (500),
        create_date VARCHAR (30),
        append_comment VARCHAR (500),
        action_sku VARCHAR (100)
        )
        """
                            )
        for i in comment_info:
            self.cursor.execute("SELECT comment_id FROM xmcomment WHERE comment_id=%s" % i['comment_id'])
            q = self.cursor.fetchone()
            if q == None:  # 判断是否以存入
                try:
                    self.cursor.execute("INSERT INTO xmcomment(comment_id,comment,create_date,append_comment,action_sku) VALUES (%s,%s,%s,%s,%s)", [i['comment_id'], i['评论'], i['评论时间'], i['追加评论'], i['商品类型']])
                except:
                    # 由于编码问题，可能会出错，所以需要修改存储字段为utf8mb4编码。
                    self.cursor.execute('ALTER TABLE xmcomment MODIFY  comment  VARCHAR(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;')
                    self.cursor.execute(
                        "INSERT INTO xmcomment(comment_id,comment,create_date,append_comment,action_sku) VALUES (%s,%s,%s,%s,%s)",
                        [i['comment_id'], i['评论'], i['评论时间'], i['追加评论'], i['商品类型']])
            else:
                print('该评论已存入数据库')
        self.conn.commit()

    def read_30(self):
        """读数据库根据rate_date倒序前30条评论的 评论"""
        self.cursor.execute('SELECT create_date, comment, append_comment FROM xmcomment ORDER BY create_date DESC ')
        data = self.cursor.fetchall()
        return data

    def jieba_word(self):
        self.cursor.execute('SELECT comment FROM xmcomment')
        comment_t = self.cursor.fetchall()
        comment_list = []
        # 取出评论数据添加到列表
        for i in comment_t:
            comment_list.append(i[0])
        comment_string = ''.join(comment_list)  # 构造长字符串
        word_list = jieba.cut(comment_string, cut_all=False)
        word = ' '.join(word_list)
        return word

    def word_jpg(self):
        word = self.jieba_word()
        font = 'simkai.ttf'
        wc = WordCloud(font_path=font,
                       background_color='white',
                       width=2000,
                       height=1500,
                       max_font_size=300,
                       min_font_size=50
                       ).generate(word)
        wc.to_file('xiaomi.png')
        print('已生成词云')

    def chart(self):
        """生成图片分析svg"""
        self.cursor.execute('SELECT DISTINCT action_sku FROM xmcomment')
        cate = self.cursor.fetchall()
        cate_list = []  # 商品类型列表
        for i in cate:
            cate_list.append(i[0])
        self.cursor.execute('SELECT COUNT(id) FROM xmcomment')
        num_all = self.cursor.fetchone()[0]  # 查询总数

        cate_num_list = []  # 构造商品类型+统计数列表
        for b in cate_list:
            self.cursor.execute(
                "SELECT COUNT(id) FROM xmcomment WHERE action_sku='%s'" % b)
            de_num = self.cursor.fetchone()[0]
            cate_num_list.append((b, de_num))

        pie_chart = pygal.Pie()
        pie_chart.title = '小米商品分析 (in %)'
        for a in cate_num_list:
            pie_chart.add(a[0], a[1] / num_all * 100)
        pie_chart.render_to_file('xiaomi.svg')


if __name__ == '__main__':
    xm = XmComment()
    xm.word_jpg()
    # data = xm.read_30()
    # print('读数据库根据rate_date倒序前30条评论的 评论')
    # for xx in data:
    #     print(xx[0])
    # print('-'*50)
    # print('\n')
    # print('正在获取评论数据')
    # num = 2  # 要保存几页
    # for i in range(1, num+1):
    #     x = xm.get_dict(i)
    #     print('正在存入数据库')
    #     xm.save_db(x)
    #     print('保存完成')
    # xm.jieba_word()
    # print('-'*50)
    # print('正在生成svg')
    # xm.chart()
    # print('生成完成→xiaomi.svg')
