# coding:utf-8
__author__ = 'trc'
# 练习
"""
目标：打开浏览器，打开百度，搜索框里面填充关键字，单击一下百度，网页向下翻，点击第二页，打印结果列表
"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# browser = webdriver.Chrome()
# browser.get("http://www.baidu.com")
# time.sleep(2)
# elemt = browser.find_element_by_id('kw')
# elemt.send_keys('python')
# elemt.send_keys(Keys.RETURN)

browser1 = webdriver.Chrome()
browser1.get('https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=48021271_22_hao_pg&wd=python&oq=%25E4%25BB%258A%25E6%2597%25A5%25E6%2596%25B0%25E9%25B2%259C%25E4%25BA%258B&rsv_pq=b63ee9f300013035&rsv_t=8ae0sznBW%2B%2BOxDAz6998pgshvk3GXZg2gASOPzmqZnmCHmu9GMjEDFe06NXZOCHErX%2BZZNOD2TJK&rqlang=cn&rsv_enter=1&rsv_sug3=6&rsv_sug1=6&rsv_sug7=101&bs=%E4%BB%8A%E6%97%A5%E6%96%B0%E9%B2%9C%E4%BA%8B')
#browser1.find_element_by_class_name('n').click()
for i in range(1,10):
    print(f'正在跳转到{i}页')
    browser1.find_element_by_xpath(f'//*[@id="page"]/a[{i}]').click()
    time.sleep(3)
    # a = browser1.find_element_by_xpath('//*[@id="content_left"]').text
    # print(a)


