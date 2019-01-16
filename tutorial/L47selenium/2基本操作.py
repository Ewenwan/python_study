# coding:utf-8
__author__ = 'trc'
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# 打开、退出浏览器，请求网页
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# time.sleep(5)
# driver.quit()

# 打开本地测试页面
# 无头模式
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options=chrome_options)
# 普通模式
browser = webdriver.Chrome()
browser.get('file:///C:/Users/Administrator/PycharmProjects/lidami/tutorial/L47selenium/2index.html')
time.sleep(3)
# 语法类似xpath、bs、js
# 1>（推荐）根据id或name获取标签，打印标签文本
# 根据 id 获取对象  相当于js中getelementById
elemt = browser.find_element_by_id("element_id")
#根据 name 获取对象
elemt1 = browser.find_element_by_name("element_id")
print(elemt)
# 2取标签中值 属性
print(elemt.text) # 标签内容
print(elemt.get_attribute('id')) # 取属性
# 3.给标签中输入文本
elemt.send_keys('自动填充一些东西')
time.sleep(2)
# 4>根据标签内容查找到标签
elemt = browser.find_element_by_link_text("find_element_by_link_text")
print(elemt.tag_name) #返回标签名
time.sleep(1)
elemt.click()#点击


# 5>根据css选择器选择元素
elemt = browser.find_element_by_css_selector(".highlight")
elemt.send_keys("啦啦啦")  # 网页的焦点并没有移动到新标签页上。
time.sleep(1)

# 6>（推荐）根据 xpath
elemt = browser.find_element_by_xpath(r'//*[@id="xpathname"]')
elemt.send_keys("我的 xpath")

# 7>跳转页面，获取页面源代码
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])
print(browser.page_source)

# 8>跳转到弹窗，接受
# 操作弹出框

elem = browser.find_element_by_tag_name("button")
elem.click()
time.sleep(1)
browser.switch_to.alert.accept()  # 切换到弹出框操作

# 9>跳转和回退操作
time.sleep(1)
elem = browser.find_element_by_link_text("forward_back")
elem.click()  # 点击跳转
time.sleep(1)
browser.back()
browser.forward() #向前方
# 10>cookies  待测试
# print(browser.get_cookies())
# # 添加一个 cookie
# browser.add_cookie({"name":"testselenium", "domian":"www.baidu.com"})
# print(browser.get_cookies())

# 11>键盘输入
elem.send_keys(Keys.RETURN)
time.sleep(3)
browser.quit() # 关闭
# 报错
# 1. selenium.common.exceptions.WebDriverException: Message: unable to set cookie
#   (Session info: chrome=71.0.3578.98)
#   (Driver info: chromedriver=71.0.3578.80 (2ac50e7249fbd55e6f517a28131605c9fb9fe897),platform=Windows NT 10.0.17134 x86_64)
# 参考：https://www.jianshu.com/p/a1a64f649472























browser.quit()