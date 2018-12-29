# 3 需要登陆的情况
"""
场景：个人信息页，订单页，需要登录权限验证后才可以访问。
权限验证：网站通过token或sessionid来限制页面访问。
sessionid：http无状态，http://www.baidu.com?kw=python,这个请求只包含目的地址和参数，不包含登录信息。登陆后只能保证本次请求，下一次请求服务器仍然不知道是否用户是否登录。为了解决用户登陆后会话保持问题，
解决方式：用户登录，服务器接收用户密码验证，通过则根据用户信息生成摘要字符串，即token或sessionid，返回响应告诉客户端保存token到cookie，浏览器接收响应后存储token到cookie，然后之后的每一次请求都会携带cookie，这样服务器就能认识客户端了。cookie好像额外的参数。token好像婚礼的请帖。
"""

"""
需求：模拟登陆，获取github 个人页/emails/  登录邮箱。

分析：直接访问个人主页会重定向到登录页。
1. 请求登录页，接收sessionid存入cookie
1) 先通过谷歌开发者工具找到login的请求（类型、url、参数）。刷新登录页，然后clear请求，然后点击登录，观察新出现的请求。
点击登录后发现https://github.com/session请求。302重定向，为了防止重定向后控制台信息被刷新掉，勾选开发者工具中的preserve log（页面重定向时保留日志不刷新）。
2) 分析登录这个请求。
路由，https://github.com/session
方法，post
参数，commit: Sign in
    utf8: ✓
    autenticity_token: SbXCFPbfNbNPNM...
    login: 1315686027@qq.com
    password: xxxx
    注意authenticity_token跟cookie中的user_sesssion不一样。authenticity_token是请求http://github/login登录页时的CSRF token，为了防止表单传出过程中被截取伪造。
    user_session是登陆成功后服务器返回的token，代表已经登录。
2. 请求个人页（携带cookie）

梳理步骤：
1. get请求 login页面
2. xpath把login页面authenticity_token获取下来，获取cookie
3. 去登录，准备好各个参数。
4. post请求 去登陆 session 第3步的参数 cookie
5. get请求 个人页
6. xpath个人页邮箱给取出
"""

import requests
from lxml import etree
import getpass
login_url = 'https://github.com/login'
do_login_url = 'https://github.com/session'
profile_url = 'https://github.com/settings/emails'

# 未登录时候请求个人页 会重定向 返回index登录表单html数据
# profile_resp = requests.get(profile_url)#,allow_redirect=False profile_resp:<Response=302>
# print(profile_resp.status_code,profile_resp.text)

headers = {
    'Host': 'github.com',
    'Referer': 'https://github.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


# requests Session会话。优点：1.保持会话，管理cookie 2.重用底层tcp连接同一网址提高效率
s=requests.session()
login_resp = s.get(login_url,headers=headers)
if login_resp.status_code !=200:
    raise Exception('get请求表达失败{}'.format(login_resp.status_code))
login_html_content=login_resp.text
# print(login_html_content)

# 匹配表单的csrf token
login_dom =etree.HTML(login_html_content)
parttern_authenticity='//input[@name="authenticity_token"]/@value'
authenticity_token = login_dom.xpath(parttern_authenticity)[0]
# print(authenticity_token)

# 请求登录接口
# 准备所需参数
session_args={
'commit': 'sgin',
'utf8': '✓',
'authenticity_token': authenticity_token,
'login': 'trclyy',
'password': 'trclyy19990222'
    # getpass.getpass("请输入密码") # 在pycharm下不可以用 需要在终端运行
}
session_resp = s.post(do_login_url,headers=headers,data=session_args)
print(session_resp.status_code)
if session_resp.status_code != 200:
     raise Exception("请求登录构造失败{}".format(session_resp.status_code))
print('登录成功')
# 请求成功后， 会话id user_token会写入到requests的cookie管理器中取，以后的请求会携带上，从而保持登录状态
# 请求个人设置页
profile_resp = s.get(profile_url, headers=headers)
# print(profile_resp.text)
with open('ssss.html', 'w', encoding='utf-8') as file:
    file.write(profile_resp.text)
if profile_resp.status_code != requests.codes.ok:
    raise Exception('请求设置个人失败')
print('请求成功')
# print(profile_resp.text)

# 获取邮箱
pattern_profile_email ='//*[@id="primary_email_select"]/option/text()'
profile_dom = etree.HTML(profile_resp.text)
profile_email=profile_dom.xpath(pattern_profile_email)
print(profile_email)

# 下节课作业，
"""
复习刚才示例的操作和分析过程
百度阅读CSRFtoken的作用和中间人攻击。
百度阅读会话token的作用和生成原理。
自己动手再分析一遍
1. github登录页
2. 在登录页源代码找到csrftoken
3. 点击登录，开发者工具中找到去登录的请求，找到请求体中的form数据
4. 登陆后查看开发者工具application中的cookie，找到会话token。
"""




