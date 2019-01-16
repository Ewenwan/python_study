import requests
import time, datetime
import logging
import json
import random
from model import Comment, CrawlLog, Product
from service.spider import Crawler
from service.word import Word
from service.pygal import Chart
from service.category import Category

from config import *
from flask import Flask, render_template, redirect, make_response



app = Flask(__name__)
app.config['DEBUG'] = DEBUG
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 10
app.logger.setLevel(level=LOGGER_LEVEL)


@app.route('/')
def hello_world():
    return

@app.route('/test')
def test():
    chart = ''
    return render_template('index.html', chart=chart)

@app.route('/third_category_product_list/<category_name>/<int:page>')
def third_category_product_list(category_name='手机', page=0, item_per_page=30):
    """ 京东三级目录商品列表 """
    context = {}
    product_list = Category.get_third_category_product_list(app=app, category_name=category_name, page=page, item_per_page=item_per_page)
    return render_template('category.html', product_list=product_list)

@app.route('/product_detail/<int:product_id>')
def product_detail(product_id=None):
    # 查询评论
    comment_objs = Word.comment_query(app=app, product_id=product_id, limit=100)    # todo 去掉limit
    if comment_objs is None:
        pass
    comment_rencent_objs = Word.comment_query(app=app, product_id=product_id, limit=10)
    # 分词
    word_cut_list = Word.cut_word(app=app, comment_objs=comment_objs)
    # 过滤停用词
    word_cut_list_clean = Word.filter_stopword(app=app, word_cut_list=word_cut_list)

    # 词云图
    word_cloud_image_url = Word.get_word_cloud_image(app=app, word_cut_list=word_cut_list_clean, output='url', width=800, height=300, max_font_size=100)

    # 分析词语情感
    word_positive_list = Word.filter_emotion(app=app, word_cut_list=word_cut_list, emotion='positive')
    # 根据情感算程度和期望
    word_emotion_degree = Word.filter_emotion_degree(app=app, word_cut_list=word_cut_list, comment_num=len(comment_objs))
    emotion_score = Word.calculate_emotion_score(app=app, word_positive_list=word_positive_list, word_emotion_degree=word_emotion_degree, comment_num=len(comment_objs))

    # 图表
    chart_word_frequency_url = Chart.chart_word_frequency(app=app, word_cut_list=word_cut_list_clean, title='高频词统计', topk=20)
    chart_word_positive_url = Chart.chart_word_positive(app=app, word_positive_list=word_positive_list, title='感情积极词统计', topk=10)
    chart_product_proportion_url = Chart.chart_product_proportion(app=app, product_id=product_id)
    chart_comment_trend_url = Chart.chart_comment_trend(app=app, product_id=product_id)
    # return render_template('index.html')
    context = {}
    context['comment_rencent_objs'] = comment_rencent_objs
    context['word_cloud_image_url'] = word_cloud_image_url
    context['chart_word_frequency_url'] = chart_word_frequency_url
    context['chart_word_positive_url'] = chart_word_positive_url
    context['emotion_score'] = emotion_score
    context['chart_product_proportion_url'] = chart_product_proportion_url
    context['chart_comment_trend_url'] = chart_comment_trend_url

    return render_template('index.html', context=context)

@app.route('/crawl_comment/<int:product_id>/<int:page_start>', methods=['GET', 'POST'])
def crawl_comment(product_id=0, page_start=0):
    if product_id < 1000000 or page_start <0 or page_start>100:
        return '参数错误'
    rs = Crawler().crawl_comment(app=app, product_id=product_id, page_start=page_start)
    return rs

@app.route('/crawl_comment/all')
def crawl_comment_by_c3():
    """ 批量爬评论
    配置从网页根据固定的config 中的三级目录product ids循环的。网页上的list接口由于回调看不到productids所以手动从
    另一个请求复制的，没仔细研究京东三级列表页
    """
    products = Product.select().where(Product.crawl_comment_num ==0)    # 没有爬过评论的
    for i, product in enumerate(products):
        if i<2:
            continue

        product_id = product.product_id
        if CrawlLog.select().where(CrawlLog.product_id==product_id, CrawlLog.success==True).count() > 10:
            print('抓取历史log大于100条跳过')
            continue

        url = 'http://127.0.0.1:5000/crawl_comment/{}/0'.format(product_id)
        resp = requests.get(url)
        print(resp.text)
        Product.update(crawl_comment_num = Product.crawl_comment_num + 10).where(Product.product_id == product_id)

        # 测试 todo
        if i == 240:
            break



if __name__ == '__main__':
    app.run()
