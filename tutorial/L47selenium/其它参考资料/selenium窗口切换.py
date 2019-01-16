# coding:utf-8
# __author__ = 'Gao'
"""
1>在同一个标签选项卡上打开不同的页面，相当于是使用同一个window窗口打开不同页面，window对象没有变；不需要切换window。
2>不同选项卡打开不同的页面，window对象会发生改变，此时注意切换window对象，否则无法定位新页面中的元素。
"""
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.get('https://www.baidu.com')

# 获取当前窗口的name
# title属性时获取<title>标签中的内容
current_window = driver.current_window_handle
print(current_window, driver.title)

# 先定位到 百度新闻 这个标签
driver.find_element_by_css_selector('a[name="tj_trnews"]').click()

# 进入到 新闻详情 页面
news = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_css_selector('.hdline0 .a3'))
news.click()

time.sleep(3)

# 获取当前程序中所有的window对象
all_window = driver.window_handles

# current_window = driver.current_window_handle
# print current_window, driver.title

# 将window对象从上一个窗口的对象，切换到新打开的window窗口对象
for window in all_window:
    if window != current_window:
        # 就是一个新的window窗口
        driver.switch_to.window(window)

news_title = WebDriverWait(driver, 30).until(lambda driver:driver.find_element_by_css_selector('.cnt_bd h1'))
print(news_title.text)

# 关闭当前新的标签页
driver.close()

# 新的标签页关闭之后，需要重新切换到上一个window，否则无法访问上一个页面中的内容了。
driver.switch_to.window(current_window)

