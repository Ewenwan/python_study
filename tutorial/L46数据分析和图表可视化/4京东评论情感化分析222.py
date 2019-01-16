# 综合项目：京东评论情感化分析
import pymysql
import jieba
import pygal
from wordcloud import WordCloud
from tutorial.L46数据分析和图表可视化.dict.degree_dict import degree_dict


CONFIG = {
    # 数据库配置
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'trc',
    'db': 'taobao',     # **
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.Cursor,  # 默认返回结果集列表套元组
    # 'cursorclass': pymysql.cursors.DictCursor,  # 返回结果集列表套字典

    # 词云配置
    'font_path': 'msyh.ttc',        # 字体文件
    'background_color': 'white',
    'width': 1000,     # 图片长
    'height': 800,
    # 'max_font_size': 300,
    'min_font_size': 50,    # 单词最小像素
    'wc_file_path': '4词云.png',  # 输出文件

    # 图表
    'chart_pie_path': '4pei.svg',

    # 其它配置
    'comment_limit': 1000   # 最多查取评论数
}


def get_cursor():
    """
    数据库连接
    :return:
    """
    try:
        connection = pymysql.connect(host=CONFIG['host'], port=CONFIG['port'],
                                     user=CONFIG['user'],
                                     password=CONFIG['password'],
                                     db=CONFIG['db'],
                                     charset=CONFIG['charset'], cursorclass=CONFIG['cursorclass']
                                     )
    except Exception as e:
        print(e, '数据库连接失败，检查用户名、密码、数据库名')
    try:
        cursor = connection.cursor()
    except Exception as e:
        print(e, '获取游标失败，上个游标已存在未关闭？')
    return cursor
def get_comments():
    """
    从数据库把所有用户评论查出
    :return: (('东西不错'),('很好'))
    """
    # 读表
    cursor = get_cursor()
    sql = """ SELECT content FROM comment order by creation_time desc limit 0, %s"""
    cursor.execute(sql, args=(CONFIG['comment_limit']))
    comments = cursor.fetchall()

    if comments:
        return comments
    else:
        print('评论结果集空')


def process_comments(comments=None):
    """
    所有用户评论拼成一个长字符串
    :param comments: (('东西不错'),('很好'))
    :return: '东西 不错 很好'
    """
    # long_string = ''
    # for comment in comments:
    #     long_string = long_string + comment[0]
    # return long_string
    return ''.join([comment[0] for comment in comments])


def cut_word(long_string):
    """
    评论内容分词
    :param string: '东西不错。真好。评论3.'
    :return: ['东西', '不错', '质量', '不错', ]
    """
    print('正在计算分词，可能需要数秒钟...')

    results = []
    word_generator = jieba.cut(long_string, cut_all=False)
    for word in word_generator:
        results.append(word)

    return results


def word_cloud(word_list):
    """
    生成词云
    :param word_list: ['东西', '不错', '质量', '不错', ]
    :return:
    """
    print('正在生成词云图')
    # 生成词云需要的string格式,空格分隔单词    '东西 不错 质量 不错'
    string = ' '.join(word_list)

    wc = WordCloud(font_path=CONFIG['font_path'],
                   background_color=CONFIG['background_color'],
                   width=CONFIG['width'],
                   height=CONFIG['height'],
                   # max_font_size=CONFIG['max_font_size'],
                   min_font_size=CONFIG['min_font_size'],
                   ).generate(string)
    wc.to_file(CONFIG['wc_file_path'])
    print('生成完毕，路径 {}'.format(CONFIG['wc_file_path']))
    return None


def chart_by_color(comments=None):
    """
    评论中购买各颜色型号比例，输出饼状图
    :return: None
    """
    assert comments is not None, 'chart_by_color方法comments参数不能为空'
    print('开始生成图表')
    # 查询
    # sql = """select count(t.id), t.product_color from (select * from comment limit 0,1000 ) as t group by product_color;"""   # 带limit版sql
    sql = """
        select count(id) as amount, product_color from comment group by product_color;
    """
    cursor = get_cursor()
    cursor.execute(sql)
    rs_set = cursor.fetchall()  # ((75,金色),(88, 灰色),(37，银色))
    if not rs_set:
        print('sql:{}  查询结果集空，无法生成饼状图'.format(sql))

    # 生成图表
    pie_chart = pygal.Pie()
    pie_chart.title = '手机销售颜色占比图（由用户评论估算）'

    amount = 0  # 购买总人数，用于计算比例
    for rs in rs_set:
        amount += rs[0]

    for rs in rs_set:
        # pie_chart.add('Firefox', 36.6)
        pie_chart.add(rs[1], round(rs[0]/amount*100, 1))
    pie_chart.render_to_file(CONFIG['chart_pie_path'])

    print('已生成图表，路径{}'.format(CONFIG['chart_pie_path']))
    # TODO get_cursor()方法封装有问题，不方便connection.close()
    return None

def filter_stopword(word_list=None):
    """
    过滤停止词
    （分词得到的列表中很多无用词汇‘的’‘，’‘。’‘；’）
    :param: word_list: ['手机', ',', '的', ]
    :return:
    """
    clean_word_list = []

    # 打开停止词字典
    with open('dict/stop_words_zh.txt', encoding='utf-8') as file:
        content = file.read()
        stop_word = content.split('\n')
    # stop_word = ['的','，','。',',', '.', '\\', '#$^@*', '地',       ' ','\n' ,'   ']

    for word in word_list:
        if word not in stop_word and word.strip() != '':
            clean_word_list.append(word)
    return clean_word_list

def count_positive_word(word_list=None, comments_amount=0):
    """
    统计积极词汇
    :param: word_list  过滤掉停用词后的分词列表
    :param: comments_amount  评论总人数
    """
    count = 0
    degree = 1

    # 打开积极词汇字典
    with open('dict/emotion_dict/pos_all_dict.txt', encoding='utf-8') as file:
        content = file.read()
        pos_word = content.split('\n')
    # pos_word = ['好', '棒', ...]

    # 统计积极词汇出现个数
    for word in word_list:
        if word in pos_word:
            count += 1

    # 统计程度词出现个数
    for word in word_list:
        if word in degree_dict.DEGREE2:
            degree += 0.5
        elif word in degree_dict.DEGREE5:
            degree += 1.5

    return count/comments_amount, degree/comments_amount

def count_negative_word(word_list=None, comments_amount=0):
    """
    统计消极词汇
    :param: word_list  过滤掉停用词后的分词列表
    :param: comments_amount  评论总人数
    """
    count = 0
    degree = 1

    # 打开消极词汇字典
    with open('dict/emotion_dict/neg_all_dict.txt', encoding='utf-8') as file:
        content = file.read()
        neg_word = content.split('\n')

    # 统计积极词汇出现个数
    for word in word_list:
        if word in neg_word:
            count += 1

    # 统计程度词出现个数
    for word in word_list:
        if word in degree_dict.DEGREE2:
            degree += 0.5
        elif word in degree_dict.DEGREE5:
            degree += 1.5

    return count/comments_amount, degree/comments_amount

def my_evaluate(positive_num=0, pos_degree_num=1, negertive_num=0, neg_degree_num=1):
    """
    我的评价
    自定计算公式，自定判断居间，返回用户评论趋势，商品销售预测结果
    :return:
    """
    score = positive_num*pos_degree_num - negertive_num*neg_degree_num
    if 0 < score < 10:
        result = '一般'
    elif score > 50:
        result = '喜欢'

    return score

if __name__ == '__main__':
    comments = get_comments()
    long_string = process_comments(comments)
    word_list = cut_word(long_string=long_string)
    # word_cloud(word_list=word_list)
    # chart_by_color(comments)
    clean_word_list = filter_stopword(word_list)
    positive_num, pos_degree_num = count_positive_word(clean_word_list, comments_amount=len(comments))
    negative_num, neg_degree_num = count_negative_word(clean_word_list, comments_amount=len(comments))
    score = my_evaluate(positive_num, pos_degree_num, negative_num, neg_degree_num)
    print(score)
    print('Done')



# 1 查所有用户评论内容
# 2 所有用户评论拼成一个长字符串
# 3 长字符串用jieba分词
# 4 拼成wordcloud使用的结构，生成评论高频关键字词云。
# 5 pygal 根据用户productcolor 统计比例，查询pygal 饼状图文档。

"""
情感化分析。通过字典方式，虽然准确度不高不过实现简单。
github中搜索关键字可以获取到相关字典（stopword.txt）。
词性：
1. 过滤掉 “停用词”、“停止词”
2. 搜索“情感词汇" "积极词汇字典” “消极词汇”
3. 读取字典到变量。
3. for循环分词后的结果，跟字典变量内容做比对。
"""

"""
# 作业：将爬虫脚本和本节图形化展示脚本集成进 django框架中
评论情感化分析
/index    展示京东手机商品列表
/product_id/12312241     触发这个商品的评论爬虫  
/result/12312241       展示分析后的图表    得出是否推荐购买
"""


