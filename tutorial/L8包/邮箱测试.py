# coding:utf-8
__author__ = 'trc'

pas2 = 'snhoakptaidkgaeb'

import smtplib
from email.mime.text import MIMEText
from email.header import Header
# msg = MIMEText('Hello,send bu python...', 'plain', 'utf-8')
from_addr = '1417633855@qq.com'  # 发送邮箱
password = pas2  # 上面生成的授权码

to_addr = 'an.shiyao@qq.com'  # 接收邮箱
to_addr2 = '1315686027@qq.com'

smtp_server = 'smtp.qq.com'  # smtp服务器
subject = 'Python email test'  # 邮件主题
msg = MIMEText('<html><h1>不要打扰我学习 小老弟</h1></html>', 'html', 'utf-8')  # 邮件内容
msg['Subject'] = Header(subject, 'utf-8')  # 编辑邮件主题
server = smtplib.SMTP()  # 生成SMTP实例
server.connect(smtp_server)  # 连接到server
server.login(from_addr, password)  # 登录到server
server.sendmail(from_addr, [to_addr, to_addr2], msg.as_string())  # 发送邮箱
server.quit()
