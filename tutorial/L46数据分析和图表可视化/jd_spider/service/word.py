import os
import re
import jieba
import jieba.analyse
import pygal
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
from model import *
from dict.degree_dict.degree_dict import *
from config import *
from flask import url_for

class Word(object):
    @classmethod
    def comment_query(cls, app=None, product_id=0, limit=None):
        """
        查询数据库comments表，返回对象
        :param app:
        :param product_id:
        :param limit: 测试少取点数据, orderby主键desc
        :return:
        """
        app.logger.debug('query obj，productid{}'.format(product_id))
        # referenceName是商品名称，相当于，下面有多种productId=referenceId，详情页url上的id就是referenceID，爬去一个productId会把所属父级referenceName下的referenceId的评论都爬下，所以先根据referenceid获取父name
        comment_obj = Comment.select(Comment.referenceName).where(Comment.referenceId == product_id).first()
        referenceName = comment_obj.referenceName
        if limit:
            comment_objs = Comment.select().where(Comment.referenceName == referenceName,
                                                  Comment.content.is_null(False)).order_by(Comment.comid.desc()).limit(limit)
        else:
            comment_objs = Comment.select().where(Comment.referenceName == referenceName, Comment.content.is_null(False))
        app.logger.debug('comment_objs条目数{}'.format(len(comment_objs)))
        return comment_objs

    @classmethod
    def cut_word(cls, app=None, comment_objs=[]):
        """
        商品评论分词
        :param product_id:
        :return: ['不错','小米',...]
        """
        # 所有评论内容放到一个字符串中
        comment_all = ''
        for comment_obj in comment_objs:
            comment_all = comment_all + comment_obj.content
        app.logger.debug('comment_all{} '.format(comment_all)[:100] + '...')

        # 分词
        cut_words = list(jieba.cut(comment_all, cut_all=False))       # 注意迭代器只能用一次

        cut_words_list = [word for word in cut_words]
        if cut_words_list is None:
            app.logger.error('cut_words_list空,检查productid在数据库中是否有对应条目')
            raise DataError
            return []
        app.logger.debug('cut_words_list{} length{}'.format(cut_words_list[:20], len(cut_words_list)))
        return cut_words_list

    @classmethod
    def filter_stopword(cls, app=None, word_cut_list=[]):
        """
        过滤停用词
        :return ['', '']
        """
        app.logger.debug('word_cut_list length{}'.format(len(word_cut_list)))
        word_cut_list_clean = []
        stop_words = []
        with open(STOPWORD_ZH_DICT, encoding='utf-8') as file:
            for line in file.readlines():
                stop_words.append(line.strip())     # 注意strip()掉换行空格
        # todo 似乎把&；也去除了导致出现在后面的统计图表中，考虑replace去换行和空格
        for word in word_cut_list:      # for in 和remove连用时注意list改变的问题
            if word not in stop_words and word.strip() != '':
                word_cut_list_clean.append(word)
        app.logger.debug('word_cut_list_clean length{}'.format(len(word_cut_list_clean)))
        return word_cut_list_clean

    @classmethod
    def filter_emotion_degree(cls, app=None, word_cut_list=None, comment_num=0):
        """
        感情程度
        例如一般、非常、太。计算情感倾向分数时用
        # 系数自己定义，步进系数 每个字典级别加一倍数值，数值越大关键字影响评分越大
        :arg comment_num: 评论数
        :return: degree(float) 每句话出现程度词的程度
        """
        digree = 0  # 程度
        k = 0.2
        for word in word_cut_list:
            if word in DEGREE1:
                digree += 1*k
            elif word in DEGREE2:
                digree += 2*k
            elif word in DEGREE3:
                digree += 3*k
            elif word in DEGREE4:
                digree += 4*k
            elif word in DEGREE5:
                digree += 5*k
            elif word in DEGREE6:
                digree += 6*k
            else:
                pass
        digree = round(digree/comment_num, 2)

        app.logger.debug('motion_degree{}'.format(digree))
        return digree

    @classmethod
    def filter_emotion(cls, app=None, word_cut_list=[], emotion=None):
        """
        过滤出积极词和消极词
        # 时间有限这里采取简单处理，为了少循环把不同程度的程度词权重都一样，没有判断反义，没有分句，跟stopword一样过了一遍字典。
        # 复杂的参考https://www.cnblogs.com/hd-zg/p/6959971.html
        # 消极词在本项目中识别率很低
        :param app:
        :param emotion: 'positive' or 'negative'
        :return: ['不错','好好'], ['坏','差',...]
        """
        app.logger.debug('filter_emotion {}'.format(emotion))

        emotion_word = []  # 情感词
        if emotion == 'positive':
            positive_word_dict = []     # 积极词字典内容
            with open(EMOTION_POSITIVE_ZH_DICT, encoding='utf-8') as file:
                for line in file.readlines():
                    positive_word_dict.append(line.strip())     # 注意strip('\n')
            for word in word_cut_list:
                if word in positive_word_dict:
                    emotion_word.append(word)
        elif emotion == 'negative':
            negative_word_dict = []     # 消极词字典内容
            with open(EMOTION_NEGATIVE_ZH_DICT, encoding='utf-8') as file:
                for line in file.readlines():
                    negative_word_dict.append(line.strip())
            for word in word_cut_list:
                if word in negative_word_dict:
                    emotion_word.append(word)
        else:
            pass
        app.logger.debug('positive_word {} length{}'.format(emotion_word[:20], len(emotion_word)))

        return emotion_word

    @classmethod
    def calculate_emotion_score(cls, app=None, word_positive_list=[], word_negative_list=[], word_emotion_degree=0, comment_num=0):
        """
        计算评分  规则：（积极词*出现次数-消极词*出现次数）* 程度指数 /评论数量  程度指数= 程度词*出现数量
        :param app:
        :param word_positive_list: 积极词列表
        :param word_negative_list:
        :param degree: 程度词指数 例如：非常、更
        :param comment_num: 原始评论总条数
        :return:
        """
        k = 111  # 值太小乘个系数
        emotion_score = 0
        word_positive_list_topk = Counter(word_positive_list).most_common(100)
        for word in word_positive_list_topk:
            emotion_score += word[1]
        emotion_score = round(emotion_score/comment_num * word_emotion_degree, 2) * k
        app.logger.debug('emotion_score{}'.format(emotion_score))
        return round(emotion_score, 2)


    @classmethod
    def get_word_cloud_image(cls, app=None, word_cut_list=[], output='url', max_words=50, width=600,
                             height=400, margin=0, max_font_size=100):
        """
        生成词云图片
        生成在static/word_cloud_image/ 目录下，返回url供前端使用
        :param app: flask app
        :param word_cut_list: jieba分词后的列表
        :param output: url链接
        :param clean: word_list过滤过停用词
        :return: url_for('static', filename='word_cloud_image/xxx.png')
        """
        word_cloud = WordCloud(max_words=max_words,
                               font_path=PATH_FONT,     # 不加这一句显示口字形乱码
                               background_color='white',
                               width=width, height=height, margin=margin, max_font_size=max_font_size,
                               stopwords=STOPWORDS)     # word_cloud包自带的停用词字典
        word_cloud_text = ' '.join(word_cut_list)   # 空格分隔
        word_cloud.generate_from_text(word_cloud_text)
        word_cloud.to_file(WORD_CLOUD_IMG)
        url_for_filename = WORD_CLOUD_IMG.replace(PATH_ROOT, '').replace('/static/', '')
        word_cloud_image_url = url_for('static', filename=url_for_filename)

        return word_cloud_image_url








