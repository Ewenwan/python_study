# 图表
import pygal
import operator
from collections import Counter
from flask import url_for
from model import *
from config import *


class Chart(object):
    @classmethod
    def chart_word_frequency(cls, app=None, word_cut_list=[], title=None, topk=20, color='green'):
        """
        高频词 条状图
        :param app:
        :param word_cut_list:
        :param title:
        :return: url('static', 'pygal_chart_images')
        """
        chart = pygal.Bar()

        word_counter_list = Counter(word_cut_list).most_common(topk)         # [('不错', 156), ('电视', 138),...]
        x_labels = [word[0] for word in word_counter_list]
        y_values = [{'value': word[1], 'color':color} for word in word_counter_list]
        chart.title = title
        chart.x_labels = map(str, x_labels)
        chart.add('频次', y_values)
        # chart_uri = chart.render_data_uri()  # base64编码的图片   注意先safe再渲染{{}}
        chart.render_to_file(filename=CHART_WORD_FREQUENCY_IMG)

        chart_url = url_for('static', filename=CHART_WORD_FREQUENCY_IMG.replace(PATH_ROOT, '').replace('/static/', ''))
        app.logger.debug('chart_word_frequency_img done {}'.format(chart_url))
        return chart_url

    @classmethod
    def chart_word_positive(cls, app=None, word_positive_list=[], title=None, topk=10, color='green'):
        """
        积极性词 条状图
        通过积极词字典筛选
        :param app:
        :param word_cut_list:  ['不错','电视'....]
        :param title:
        :param topk:
        :param color:
        :return:
        """
        chart = pygal.Bar()
        word_counter_list = Counter(word_positive_list).most_common(topk)  # [('不错', 156), ('电视', 138),...]
        x_labels = [word[0] for word in word_counter_list]
        y_values = [{'value': word[1], 'color': color} for word in word_counter_list]
        chart.title = title
        chart.x_labels = map(str, x_labels)
        chart.add('频次', y_values)
        chart.render_to_file(filename=CHART_WORD_POSITIVE_IMG)

        chart_url = url_for('static', filename=CHART_WORD_POSITIVE_IMG.replace(PATH_ROOT, '').replace('/static/', ''))
        app.logger.debug('chart_word_positive_img done {}'.format(chart_url))
        return chart_url

    @classmethod
    def chart_product_proportion(cls, app=None, product_id=0, title='此颜色型号占所有销量百分比'):
        """
        这个颜色型号占这个商品百分比 饼状图。这个referenceId占title下所有referenceId的百分比
        :param app:
        :param product_id: referenceId 由productColor productSize决定
        :return:
        """
        # referenceName是商品名称，相当于，下面有多种productId=referenceId，详情页url上的id就是referenceID，爬去一个productId会把所属父级referenceName下的referenceId的评论都爬下，所以先根据referenceid获取父name
        comment_obj = Comment.select(Comment.referenceName, Comment.productColor, Comment.productSize).where(Comment.referenceId == product_id).first()
        if comment_obj is None:
            raise RuntimeError
        referenceName = comment_obj.referenceName
        productColor = comment_obj.productColor
        productSize = comment_obj.productSize
        product_count = Comment.select().where(Comment.referenceId == product_id, Comment.content.is_null(False)).count()
        all_count = Comment.select().where(Comment.referenceName == referenceName, Comment.content.is_null(False)).count()
        if all_count != 0:
            proportion = product_count / all_count * 100    # 百分比
        app.logger.debug('chart_product_proportion {:.2f}'.format(proportion))

        chart = pygal.Pie()
        chart.title = title
        chart.add(productColor+productSize, round(proportion, 2))
        chart.add('其它', 100-round(proportion, 2))
        chart.render_to_file(filename=CHART_PRODUCT_PROPORTION_IMG)
        chart_url = url_for('static', filename=CHART_PRODUCT_PROPORTION_IMG.replace(PATH_ROOT, '').replace('/static/', ''))
        app.logger.debug('chart_product_proportion done {}'.format(chart_url))
        return chart_url

    @classmethod
    def chart_comment_trend(cls, app=None, product_id=0, title='人们喜欢上京东的时间规律', limit=1000):
        """
        评论按小时统计次数展示最近几小时  折线图
        # 因为抓爆款商品一百页评论时间上只有三天，所有数据不够分析评论趋势。需求改为上京东时间规律，预计早中晚多。
        :param app:
        :param product_id:
        :param title:
        :return:
        """
        comment_objs = Comment.select().where(Comment.referenceId == product_id, Comment.content.is_null(False)).\
            order_by(Comment.creationTime.desc()).limit(limit)

        time_hour_list=[]
        for comment in comment_objs:
            creationTime = comment.creationTime
            create_time_hour = creationTime.hour
            time_hour_list.append(create_time_hour)
        comment_trend_counter = Counter(time_hour_list).most_common(24)
        comment_trend_counter = sorted(comment_trend_counter,key=operator.itemgetter(0), reverse=True)    # 不能用sort
        app.logger.debug('chart_comment_trend {}'.format(comment_trend_counter))

        chart = pygal.Line()
        chart.title = title
        chart.x_labels = [c[0] for c in comment_trend_counter]
        chart.add('评论人次/小时', [c[1] for c in comment_trend_counter])
        chart.render_to_file(filename=CHART_COMMENT_TREND_IMG)
        chart_url = url_for('static',
                            filename=CHART_COMMENT_TREND_IMG.replace(PATH_ROOT, '').replace('/static/', ''))
        app.logger.debug('chart_comment_trend done {}'.format(chart_url))
        return chart_url



# 图表
# 高频top20 bar；积极频次10；用户评论活跃时间；商品购买比例；
# 消极频次  差评率仅占2%，消极词语往往连成句子，不容易被字典判断出来。
# 三个月购买量趋势  无法完成，两天评论量都一百页了，最多采集一百页。

