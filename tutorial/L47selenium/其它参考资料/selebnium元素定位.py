# coding:utf-8
# __author__ = 'Gao'

from selenium import webdriver

# 一定将geckodriver.exe和chromedriver.exe这两个驱动放到环境变量PATH中，就和python.exe放在一起。
# executable_path="E:/driver/geckodriver"用于指定火狐、谷歌驱动的可执行路径
driver = webdriver.Firefox()

# 通过标签的id属性进行定位元素
driver.get('http://www.baidu.com')

# 定位输入框
# selenium中提供的find_element_by_XXX这些方法都是纯Python语言实现的。如果只是定位和查找元素，建议使用lxml中的xpath或者cssselect方式。
# 如果需要对元素进行点击，输入，滚动等浏览器操作时，建议使用find_element_by_XXX这些方法。
# driver.find_element_by_id('kw').send_keys(u'selenium')

# 通过name属性定位元素
# driver.find_element_by_name('wd').send_keys(u'123')

# 通过class属性定位元素
# driver.find_element_by_class_name('s_ipt').send_keys(u'111')

# 通过标签名定位元素
# driver.find_element_by_tag_name('input')

# 通过css选择器定位元素
# driver.find_element_by_css_selector('#form #kw')

# 通过xpath定位元素
# driver.find_element_by_xpath('//form[@id="form"]/span/input[@id="kw"]')

# 通过link连接定位元素
# 通过一个链接上面展示的文本，来定位到这个标签。
res = driver.find_element_by_link_text('贴吧')

# selenium.webdriver.firefox.webelement.FirefoxWebElement
print res
