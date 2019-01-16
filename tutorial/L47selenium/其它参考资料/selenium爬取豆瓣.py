# coding:utf-8
# __author__ = 'Gao'

# 爬取豆瓣电影网高分电影及热门影评

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://movie.douban.com/'

# 获取电影详情地址以及电影的名称
def get_detail_url_and_movie_name(movie_count):
    # 定位 “选电影” ，
    driver_info.get(url)
    WebDriverWait(driver_info, 10).until(lambda driver_info:driver_info.find_elements_by_css_selector('.nav-items a')[1]).click()
    # 定位 “豆瓣高分” 选项
    WebDriverWait(driver_info, 10).until(lambda driver_info:driver_info.find_elements_by_css_selector('.tag-list label')[4]).click()

    # 需要根据电影总数量，计算需要点击几次“加载更过”，下载电影信息
    # open_more变量用于记录点击次数
    open_more = movie_count/20 - 1
    print open_more
    # 定位加载更多
    for x in xrange(1, open_more+1):
        WebDriverWait(driver_info, 10).until(lambda driver_info: driver_info.find_element_by_css_selector('.more')).click()
        # 提取电影名称
        a_list = driver_info.find_elements_by_css_selector('.item')
        for a in a_list:
            print u"电影地址："+a.get_attribute('href')
            print u"电影名称："+a.text
            # 根据电影详情url下载热门评论
            get_detail_info(a.get_attribute('href'))

def get_detail_info(url):
    driver_detail.get(url)
    div = WebDriverWait(driver_detail, 10).until(lambda driver_detail:driver_detail.find_element_by_css_selector('#hot-comments'))
    comments_list = div.find_elements_by_class_name('comment-item')
    # 获取前5条热门评论
    for comment in comments_list[:5]:
        # 在comment这个对象的基础上继续定位p标签
        p = comment.find_element_by_tag_name('p').text
        print u'热门评论：'+p


if __name__ == "__main__":
    # 创建两个Phantomjs浏览器对象，一个用于解析列表页，一个用于解析详情页的热门评论。
    driver_info = webdriver.PhantomJS()
    driver_detail = webdriver.PhantomJS()
    # 输入需要下载的数量
    number = input('请输入下载总数：')
    get_detail_url_and_movie_name(number)
