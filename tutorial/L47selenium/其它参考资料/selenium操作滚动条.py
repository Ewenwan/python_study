# coding:utf-8
# __author__ = 'Gao'

# 如果定位的元素在页面的下方不可见位置，需要对页面的滚动条进行操作，才能正确的定位到该元素。
import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.baidu.com')

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()

time.sleep(2)

# 方法一：
# 将滚动条滚动到页面底部
# js = "document.documentElement.scrollTop=10000" # 针对Firefox有效
# # js = "document.body.scrollTop=10000" # 针对Chrome有效
# driver.execute_script(js)

# 将滚动条滚动到页面顶部
# js = "document.documentElement.scrollTop=0"
# driver.execute_script(js)

# 方法二：
target = driver.find_element_by_xpath('//div[@id="3"]/h3/a')
# 将滚动条滚动到可视范围内，只要能够定位该元素即可。
# scrollIntoView(false): 参数false是指元素不会滚动到页面顶部，只要在View页面显示即可。
# arguments[0]: 指代的就是target，就是我们需要定位的元素
driver.execute_script("arguments[0].scrollIntoView(false);", target)

time.sleep(5)

print '----',target
target.click()
