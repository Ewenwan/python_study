# coding:utf-8
# __author__ = 'Gao'

# 如果通过selenium方法，一次性选中多个标签元素。
import os
from selenium import webdriver

# 引入By模块
from selenium.webdriver.common.by import By

# print os.path.abspath(os.getcwd())
# print os.path.abspath('html/checkbox.html')

driver = webdriver.Firefox()
#
# # 通过driver访问本地.html文件
driver.get('file:///' + os.path.abspath('html/checkbox.html'))

# 第一种方法
# 先选出所有的input标签，然后通过属性type对input进行过滤
# inputs = driver.find_elements_by_tag_name('input')
# print inputs
#
# for input in inputs:
#     if input.get_attribute('type') == 'checkbox':
#         input.click()

# 第二种方法
# pop()方法是用于去除列表中的一个元素
# driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()

# find_element()和find_elements()

# by: 通过什么方式进行查找 ID CLASS_NAME TAG_NAME
# value: 选择器的值
input_c1 = driver.find_element(by=By.ID, value="c1")
input_c1.click()

