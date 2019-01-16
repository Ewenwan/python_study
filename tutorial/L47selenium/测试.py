# coding:utf-8
__author__ = 'trc'
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome()
chrome.get("http://www.baidu.com")
time.sleep(2)
elemt = chrome.find_element_by_id('kw')
elemt.send_keys('python')
elemt.send_keys(Keys.RETURN)
search_btu = chrome.find_element_by_id('su')
search_btu.click()
# 拖动滚动条
for x in range(1, 10):
    time.sleep(0.2)
    j = x/10
    js = 'document.documentElement.scrolltop = document.documentElement.scrollHeight * %f' % j
    chrome.execute_script(js)

# 点击下一页
chrome.find_element_by_class_name('n').click()
# 打印内容
s = chrome.find_element_by_class_name('container_s')
b=s.text
print(b)

