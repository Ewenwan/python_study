# coding:utf-8
# __author__ = 'Gao'

# 比如：一个网页在通过selenium的浏览器打开的时候，由于网络慢等原因导致页面一直处在加载的过程当中，页面中的一些标签可能没有渲染出来，由于代码的执行速度比较快，当通过代码去查找元素时，页面的元素可能不存在。这时候程序会出现 NoSuchElementException异常。

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Firefox()
browser.get("https://www.baidu.com")

# print '开始休眠'
# time.sleep()让线程休眠一定的时间，等休眠时间到了之后，不管元素是否找到，仍然强制往后执行。
# 一般这种方式调试的时候，经常用，代码中尽量少用，会影响程序的执行效率。
# time.sleep(10)
# print '休眠结束'


# WebDriverWait该类是用于设置显性等待，经常配合着until()和until_not()函数而使用，在页面加载期间，每隔一定的时间去查看元素是否已经被加载出来，如果没有加载出来，则继续等待，直到超出最大等待时间，最后还没有发现该元素，则最终抛出异常。如果在最大时间范围内找到了该元素，则继续往后执行代码。
print '开始查找'

# a_search = WebDriverWait(browser, 30).until(lambda browser:browser.find_element_by_xpath('//input[@id="kw"]'))

# 一般在代码中可能标签已经存在了，但是浏览器的页面上还没有渲染出来，
# 这种情况下，通过find_element_by_XXX是可以找到该标签的，但是不能点击。
button = browser.find_element_by_id('su') # 登录按钮
# is_displayed()用于判断一个标签是否在浏览器页面上显示出来。
is_visiable = WebDriverWait(browser, 10).until(lambda browser:button.is_displayed())
print is_visiable
# 让button元素在10s时间内进行循环检测，直到返回True，说明浏览器显示该按钮了
button.click()
# ElementNotVisiableException: 元素不可见异常

print '查找结束'
# print a_search

# 以Anaconda官网为例
# a_element = browser.find_element_by_xpath('//a[@data-accordion="#top-search"]')
# print a_element
# a_element.click()

# 设置隐性等待时间
# 隐性等待，和time.sleep类似，设置一个最长等待时间，如果网页在规定的时间内加载完成，则执行下一步，否则会一直处于等待状态，知道超时。一般一个程序内只调用一次该方法即可。
browser.implicitly_wait(30)
browser.find_element_by_id('kw').send_keys('123')

# 隐性等待implicitly_wait和显性等待WebDriverWait的区别：
# 1>implicitly_wait是针对一个页面，一个会话窗口而言，是在等待该页面上所有的元素被加载完成，而不是针对某一标签元素。等页面上的各个元素渲染完成之后，再进行查找和定位。
# 2>WebDriverWait是针对某一个元素而言，不是在等待整个页面元素的渲染完成，而只是等待这一个元素是否渲染完成，然后去定位该元素。所以，每一个元素都可以使用它判断是否出现。
