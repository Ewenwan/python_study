# coding:utf-8
# __author__ = 'Gao'

import time, os

import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

cookie = ''
def login():
    global cookie
    if os.path.exists('cookies.txt') == False:
        # 本地没有Cookie文件，则进行登录
        driver = webdriver.Firefox()
        driver.get('https://www.zhihu.com/signup')

        # 定位到登录按钮，切换输入用户名和密码模式
        driver.find_element_by_css_selector('.SignContainer-switch>span').click()

        # 输入用户名和密码
        driver.find_element_by_css_selector('input[name="username"]').send_keys('17737713931')
        driver.find_element_by_css_selector('input[name="password"]').send_keys('gao12345')

        # 需要判断页面中是否存在验证码，如果有验证码则识别输入，如果没有验证码则直接登录
        # 通过观察img标签的src属性，发现有验证码时src="data:image/jpg;base64,RO1XXXX"，没有验证码时src="data:image/jpg;base64,null"，可以根据src属性中是否包含null来判断本次登录是否有验证码。
        # captcha_img_src = driver.find_element_by_css_selector('.Captcha-chineseImg').get_attribute('src').encode('utf-8')
        captcha_img_src = driver.find_element_by_xpath('//div[contains(@class, "Captcha")]//img[starts-with(@class, "Captcha")]').get_attribute('src').encode('utf-8')
        if 'null' in captcha_img_src:
            print '没有验证码'
        else:
            print '有验证码'
            # 进一步区分是中文验证码还是英文验证码
            # 通过验证码所在div，它的类名的变化进行区分：如果中文验证码<div class="Captcha-chinese">。如果是英文验证码div标签中没有chinese字符。
            try:
                div = driver.find_element_by_css_selector('.Captcha-chinese')
            except NoSuchElementException, e:
                div = None
            if div:
                print '中文验证码'
                driver.quit()
                # 中文验证码时，退出当前登录操作，关闭浏览器。然后再次调用登录函数login()，直到没有验证码或者英文验证码再登录。
                login()
            else:
                print '英文验证码'
                # 可以通过PIL模块对验证码进行截图，上传到云打码进行识别，将识别的结果输入到验证码输入框中，最后点击登录按钮。
                driver.quit()
                login()

        # 定位到登录按钮，进行登录
        driver.find_element_by_css_selector('.SignFlow-submitButton').click()

        # 登录成功之后，获取cookie信息，并将cookie信息保存到本地
        # print driver.get_cookies()

        # 登录之后休眠，防止cookie只加载一部分。
        time.sleep(3)

        cookie = [item['name'].encode('utf-8') + '=' + item['value'].encode('utf-8') for item in driver.get_cookies()]
        cookie = ';'.join(cookie)
        with open('cookies.txt', 'w') as f:
            f.write(cookie)
        # 退出浏览器
        driver.quit()
    else:
        # 有cookie，免登录
        with open('cookies.txt', 'r') as f:
            cookie = f.read()
        print '加载本地cookie'

    # 利用cookie信息，获取知乎首页的内容
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0",
        "HOST": "www.zhihu.com",
        "Authorization": "oauth c3cef7c66a1843f8b3a9e6a1e3160e20",
        "Cookie": cookie,
    }
    response = requests.get('https://www.zhihu.com/', headers=headers)
    print response.content


if __name__ == "__main__":
    login()
