# coding:utf-8
# __author__ = 'Gao'

# selenium 是一个用于对web网页进行自动化测试的工具，可以通过它提供的一些方法自动操作浏览器，可以完全模拟人的操作。

# selenium在Python爬虫中的应用：
# 1>获取动态网页中的数据，一些动态的数据我们在获取的源码中并没有显示的这一类动态加载数据；
# 2>用于模拟登录，一些比较复杂的登录过程，如果不通过selenium中的浏览器驱动完成登录的话，我们需要分析出来这个登录发起的所有请求之间关联包括cookie等关键信息(比如知乎登录)，而通过selenium驱动浏览器来完成知乎登录的话，就不需要考虑一些cookie，请求和请求之间的关联等信息，只需要用户名密码即可登录。

# selenium的特点：
# 1.它是通过驱动浏览器来进行页面登录，或者是获取页面信息；
# 2.通过selenium来爬取网站的时候，效率比较低，因为浏览器的打开，请求，渲染页面都需要一定的时间，所以尽量少使用selenium进行网站爬取，除非是动态网站。
# 3.selenium提供的一些用于元素定位和查找的API都是纯Python语言实现的，所以效率上看，没有lxml中的定位API效率高。
# 4.selenium是开源免费的，支持主流的浏览器，IE，FireFox，Chrome，Opera，Safari等。

# 安装selenium: pip install selenium
# 安装浏览器驱动，用于启动浏览器：firefox driver, chrome driver。

from selenium import webdriver

# 创建一个火狐浏览器对象
browser = webdriver.Chrome()
# browser = webdriver.Firefox()

# 通过浏览器对象browser向某一个url发起请求
browser.get('https://www.baidu.com')

# 定位到输入框，输入数据
# send_keys：向输入框中输入关键信息
browser.find_element_by_id('kw').send_keys('selenium下载')

# 点击右侧的百度一下, click()按钮的点击事件
browser.find_element_by_id('su').click()

# //*[@id="su"] #su
# //*[@id="kw"]
# //*[@id="form"]