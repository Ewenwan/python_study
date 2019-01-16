# coding:utf-8
# __author__ = 'Gao'

# 对于一个web网站来说，有时候会遇到页面中含有内联框架iframe或者另一个窗口window，我们在去定位框架或者窗口中的标签时，直接通过find_element_by_*是无法直接定位的。必须先从外层窗口切换到内层窗口，然后再去查找。
import os,time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

file_path = 'file:///' + os.path.abspath('html/frame.html')
driver.get(file_path)
# switch_to.frame(frame_reference): 切换iframe框架的方法，参数frame_reference是用于定位iframe，可以传ID, NAME等。还可以传递一个webElement对象
driver.switch_to.frame(driver.find_element_by_css_selector('iframe'))
# driver.switch_to.frame('f1')

# 再切换到第二层iframe
driver.switch_to.frame('f2')

driver.find_element(by=By.ID, value='kw').send_keys(u'selenium')
driver.find_element(by=By.ID, value='su').click()



