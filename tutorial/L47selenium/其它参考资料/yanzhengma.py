# coding:utf-8
# __author__ = 'Gao'

# 通过验证码在线识别之后，将用户名，密码，验证码的值进行模拟登录，登录成功之后需要将登陆之后的cookie信息存储到本地，以后在一段时间内直接可以携带cookie进行免登录了。

import cookielib

import requests
from lxml import etree
from fake_useragent import UserAgent

from YDMHTTPDemo import yan_zheng

session = requests.Session()
session.cookies = cookielib.LWPCookieJar(filename='cookie.txt')
try:
    session.cookies.load(ignore_expires=True, ignore_discard=True)
except Exception, e:
    print '本地还没有cookie.txt文件'

ua = UserAgent()
headers = {
    'User-Agent': ua.random,
}

def get_captcha():
    response = session.get('http://www.yundama.com/index/captcha', headers=headers)
    # 而response响应体中就是一张图片
    with open('captcha.jpeg', 'wb') as f:
        f.write(response.content)

def login_ydm():
    # 登录前，先获取验证码图片上的字符串
    get_captcha()

    # 将本地的验证码图片进行YDM在线验证
    cid, result = yan_zheng('captcha.jpeg')
    # print cid
    # print result

    # 使用验证码进行登录
    response = session.get('http://www.yundama.com/index/login?username=gaohairui&password=gao12345&utype=1&vcode={}'.format(result), headers=headers)
    session.cookies.save(ignore_discard=True, ignore_expires=True)

# login_ydm()

# 通过cookie访问首页信息
def index():
    response = session.get('http://www.yundama.com/user', headers=headers)
    html = etree.HTML(response.content)

    # 提取登陆后的用户名
    res = html.xpath('//p[@class="op_user_txt"]//text()')
    print res

index()
