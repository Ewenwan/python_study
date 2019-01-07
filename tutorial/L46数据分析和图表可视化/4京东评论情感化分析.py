# 综合项目：京东评论情感化分析
import pymysql


# 1 从数据库把所有用户评论查出
def get_comments():
    # 连接数据库
    # 读表
    # select content from
    connect = pymysql.connect(user='root', password='trc', db='jddd')
    cursor = connect.cursor()
    cursor.execute("""select content from jdjd""")
    comment = cursor.fetchall()
    return comment
def process_comments(comment):
    # 所有用户评论拼成一个长字符串
    list1 = []
    for i in comment:
        list1.append(i[0])
    # print(list1)
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
    wc.to_file('京东评论1.png')
def gen_pei():
    # 生成饼状图
    # select count() group by
    # 本地生成饼状图
    connect = pymysql.connect(user='root', password='trc', db='jddd')
    cursor = connect.cursor()
    cursor.execute("SELECT COUNT(productColor) FROM jdjd WHERE productColor='金色'")
    gold = cursor.fetchone()
    cursor.execute("SELECT COUNT(productColor) FROM jdjd WHERE productColor='银色'")
    silver = cursor.fetchone()
    cursor.execute("SELECT COUNT(productColor) FROM jdjd WHERE productColor='深空灰色'")
    gray = cursor.fetchone()
    print('正在生成饼状图')
    pie_chart = pygal.Pie()
    pie_chart.title = '苹果手机颜色分析'
    pie_chart.add('金色', gold[0] / 200)
    pie_chart.add('银色', silver[0] / 200)
    pie_chart.add('深空灰色', gray[0] / 200)
    pie_chart.render_to_file('test.svg')
if __name__ == '__main__':
    comment = get_comments()
    str  =process_comments(comment)
    result = cut_word(str)
    pei =word_cloud(result)
    gen_pei=gen_pei()

