# coding:utf-8
__author__ = 'trc'
import json
import pymysql
import jieba
import pygal
from wordcloud import WordCloud


def get_content():
 with open('tb_comments_1.json', encoding='utf-8') as f:
        comments = json.load(f)
        comment = comments['rateDetail']['rateList']
        comment_list = []
        for i in comment:
                comment = i['rateContent']
                rateDate = i['rateDate']
                id = int(i['id'])
                auctionSku = i['auctionSku']
                if i['appendComment'] == None:
                    appendComment = '用户没有追加评论'
                else:
                    appendComment = i['appendComment']['content']
                comment_list.append(
                    {'评论': comment, '评论时间': rateDate, 'comment_id': id, '商品类型': auctionSku, '追加评论': appendComment})
        return comment_list
def save(comment_list):
            conn = pymysql.connect(user='root', password='trc', host='127.0.0.1', db='taobao')
            cursor = conn.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS comment(id INTEGER PRIMARY KEY,comment_id bigint ,rate_content VARCHAR(500),rate_date  DATETIME,append_content varchar(500),action_sku varchar(50))')
            y=1
            for i in comment_list:
                print(f'正在保存第{y}页')
                cursor.execute('INSERT INTO comment (id,comment_id,rate_content,rate_date,append_content,action_sku) VALUES (%s,%s,%s,%s,%s,%s)',[y, i['comment_id'], i['评论'], i['评论时间'],i['追加评论'],i['商品类型']])
                y += 1
            conn.commit()
            conn.close()
def get_comments():
    # 连接数据库
    # 读表
    # select content from
    connect = pymysql.connect(user='root', password='trc', db='taobao')
    cursor = connect.cursor()
    cursor.execute("""select rate_content,append_content from comment""")
    comment = cursor.fetchall()
    return comment
def process_comments(comment):
    # 所有用户评论拼成一个长字符串
    list1 = []
    for i in comment:
        list1.append(i[0])
    str1 = ''.join(list1)
    return str1
def cut_word(str1):
    # 分词，返回wordcloud包使用的格式
    results = jieba.cut(str1, cut_all=False)
    word_list = []
    for r in results:
        word_list.append(r)
    print(word_list)
    www = ' '.join(word_list)
    return www
def word_cloud(results):
    # 生成词云，保存到本地
    font = 'msyhbd.ttc'
    wc = WordCloud(font_path=font,  # 如果是中文必须要添加这个
                   background_color='blue',
                   width=3000,
                   height=2500,
                   max_font_size=300,
                   min_font_size=50).generate(results)
    wc.to_file('淘宝评论.png')
def bingzhuang():
        conn = pymysql.connect(user='root', password='trc', host='127.0.0.1', db='taobao')
        cursor = conn.cursor()
        cursor.execute('SELECT DISTINCT action_sku FROM comment') # DISTINCT 不重复distinct
        cate =cursor.fetchall()
        cate_list = []
        for i in cate:
            cate_list.append(i[0])
        cursor.execute('SELECT COUNT(id) FROM comment')
        num_all = cursor.fetchone()[0]  # 查询总数

        cate_num_list = []  # v构造商品类型+统计数列表
        for b in cate_list:
            cursor.execute(
                "SELECT COUNT(id) FROM comment WHERE action_sku='%s'" % b)
            de_num = cursor.fetchone()[0]
            cate_num_list.append((b, de_num))

        pie_chart = pygal.Pie()
        pie_chart.title = '小米商品分析 (in %)'
        for a in cate_num_list:
            pie_chart.add(a[0], a[1] / num_all * 100)
        pie_chart.render_to_file('小米手机评论.svg')


if __name__ == '__main__':
    # comment_list =get_content()
    # yy =save(comment_list)
    comments =get_comments()
    process_comments=process_comments(comments)
    cut_word =cut_word(process_comments)
    word_cloud=word_cloud(cut_word)
    bingzhuang()
