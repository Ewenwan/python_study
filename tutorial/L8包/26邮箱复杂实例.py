# coding:utf-8
__author__ = 'trc'

import yagmail
import os

sender ='1417633855@qq.com'
password ='snhoakptaidkgaeb' # 授权密码
target ='1315686027@qq.com'
html = """
<html lang="zh">
    <head>
        <meta charset="utf-8">
        <title>大米米</title>
    </head>
    <body>
        <hl>大米米</hl>
        <p>lovelovelovelovelovelove</p>
        <img src="https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1181602451,3474337811&fm=26&gp=0.jpg"/>
    </body>
</html>
"""
attachment_path = os.path.join(os.path.dirname(__file__),'yy.jpg')
contents = ['love', html,attachment_path]
yag = yagmail.SMTP(user=sender,password=password,host='smtp.qq.com',smtp_ssl=True)
yag.send(to=target,subject='love',contents=contents)
print('给李大米发邮件成功')