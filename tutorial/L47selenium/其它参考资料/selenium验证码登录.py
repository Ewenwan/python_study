# coding:utf-8
# __author__ = 'Gao'

import time
from YDMHTTPDemo import yan_zheng
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# PIL是用于对图片进行操作的一个第三方库，anaconda集成工具中默认已经安装了pillow，可以直接使用pillow库中的PIL。
# 需要安装时：pip install pillow
# PIL实现对图片的旋转，缩放，剪切，放大缩小等操作。
from PIL import Image

driver = webdriver.Firefox()
driver.get('https://ics.autohome.com.cn/passport/account/login')

# 定位用户名输入框
username = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_id('UserNameDealer'))
username.send_keys(u'元信汽车')

# 定位密码输入框
password = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_id('PasswordDealer'))
password.send_keys('layx2012,')

# 定位验证码标签，对验证码实现截图功能。
captcha = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_id('imgValidCodeDealer'))
# 验证码截取策略：
# 1>将整个网页的内容全部截取下来；
# 2>再根据验证码图片在整个网页中的x坐标和y坐标，以及图片自身的宽度和高度，从整个网页的截图中再截取验证码图片；

# 截取整个页面
driver.save_screenshot('page.png')

# 获取验证码图片的x, y坐标，及自身宽度和高度
left = captcha.location['x']
top = captcha.location['y']
right = captcha.location['x'] + captcha.size['width']
bottom = captcha.location['y'] + captcha.size['height']

# print left, top, right, bottom

# 截取验证码
img = Image.open('page.png')
img = img.crop((left, top, right, bottom))
# 保存到本地
img.save('captcha.png')

# 将验证码图片上传到云打码进行在线识别
text = yan_zheng('captcha.png')

captcha_input = driver.find_element_by_id('checkCodeDealer')
captcha_input.send_keys(text)

# 登录按钮
driver.find_element_by_id('btnDealer').click()

time.sleep(5)
# 登录之后，休眠一定的时间之后再获取网页源代码，因为页面的渲染需要时间。
print driver.page_source

