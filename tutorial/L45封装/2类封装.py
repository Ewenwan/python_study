# 练习
import requests
import getpass
from lxml import etree

class Github(object):
    def __init__(self):
        # 属性 公共 全局需要访问  后面可以通过self.访问
        self.login_url = 'https://github.com/login'
        self. do_login_url = 'https://github.com/session'
        self.profile_url = 'https://github.com/settings/emails'
        self.name_url='https://github.com/trclyy?tab=repositories'
        self.headers={'Host': 'github.com',
    'Referer': 'https://github.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        self.s =requests.Session()
    def get_csrf_token(self):
        # 请求表单页
        resp = self.s.get(self.login_url)
        html_content = resp.text
        pattern = '//input[@name="authenticity_token"]/@value'
        dom = etree.HTML(html_content)
        authenticity_token =dom.xpath(pattern)[0]
        return authenticity_token
    def do_login(self,authenticity_token):
        """
        去登录
        :param authenticity_token: 组装请求所需
        :return:
        """
        params ={
            'commit': 'sgin',
            'utf8': '✓',
            'authenticity_token': authenticity_token,
            'login': 'trclyy',
            'password': 'trclyy19990222'
        }
        session_resp = self.s.post(self.do_login_url,headers=self.headers,data=params)
        if session_resp.status_code != 200:
            raise Exception("请求登录构造失败{}".format(session_resp.status_code))
        print('登录成功')
    def request_profile(self):
        """
        请求个人设置页 {str}
        :return:
        """
        profile_resp = self.s.get(self.profile_url, headers=self.headers)
        # print(profile_resp.text)
        if profile_resp.status_code != requests.codes.ok:
            raise Exception('请求设置个人失败')
        print('请求成功')
    def get_email(self):
        profile_resp = self.s.get(self.profile_url, headers=self.headers)
        pattern_profile_email = '//*[@id="primary_email_select"]/option/text()'
        profile_dom = etree.HTML(profile_resp.text)
        profile_email = profile_dom.xpath(pattern_profile_email)
        print(profile_email)
    def get_gitname(self):
        resp = self.s.get(self.name_url,headers=self.headers).text
        for i in range(1,3):
            name = f'//*[@id="user-repositories-list"]/ul/li[{i}]/div[1]/div[1]/h3/a /text()'
            profile_dom = etree.HTML(resp)
            profile_name = profile_dom.xpath(name)[0]
            print(f'第{i}个数据库的名字是:{profile_name}')
if __name__ == '__main__':
    github = Github()
    authenticity_token=github.get_csrf_token()
    github.do_login(authenticity_token)
    github.get_email()
    github.get_gitname()