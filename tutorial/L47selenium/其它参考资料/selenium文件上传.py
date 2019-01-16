# coding:utf-8
# __author__ = 'Gao'

# 通过selenium上传本地文件，一般先定位到网页中的上传按钮，通过send_keys()方法添加本地文件到网页中即可。在send_keys时一般会打开一个本地窗口用于选择本地文件。

import os
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('file:///' + os.path.abspath('html/upload.html'))

# 定位上传按钮, 添加本地文件
driver.find_element_by_tag_name('input').send_keys(u'html/inner.html')

