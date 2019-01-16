# coding:utf-8
# __author__ = 'Gao'

# webdriver中常用的对象操作事件和属性
# 1>click() 对象点击事件，点击一个按钮
# 2>send_keys() 向输入框中输入文本
# 3>clear() 清除文本内容
# 4>text 用于获取元素的文本信息
# 5>get_attribute() 用于获取标签元素的属性信息

from selenium import webdriver

driver = webdriver.Firefox()

# driver.get('http://www.yundama.com/')
#
# # 定位用户名和密码输入框
# driver.find_element_by_id('username').clear()
# driver.find_element_by_id('username').send_keys('gaohairui')
#
# driver.find_element_by_id('password').clear()
# driver.find_element_by_id('password').send_keys('gao12345')
#
# content = driver.find_element_by_class_name('hover').text
# print '文本内容：', content
#
# attr = driver.find_element_by_css_selector('.hover').get_attribute('class')
# print '属性：', attr

# 模拟快捷键
import time
from selenium.webdriver.common.keys import Keys

# send_keys(Keys.TAB) :相当于按下键盘上的tab键
# send_keys(Keys.ENTER) :相当于按下键盘上的Enter回车键

driver.get('https://www.baidu.com')

driver.find_element_by_id('kw').send_keys('selenium test')

time.sleep(3)

# 通过组合键复制输入框中输入的内容
# Keys.CONTROL, 'a'  相当于使用了组合键 control + a: 全选
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')

time.sleep(3)

# Keys.CONTROL, 'x': control+x剪切
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

time.sleep(3)

driver.find_element_by_id('kw').send_keys('chromedriver')

time.sleep(3)

# 退出浏览器
driver.quit()
