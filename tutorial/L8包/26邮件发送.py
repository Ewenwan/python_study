# coding:utf-8
__author__ = 'trc'

# 邮件发送
# 场景：工作沟通邮件；登录注册；广告；修改密码、激活链接；邮件客户端。
# 参考 https://www.1owo.com/python/python/python-python%E5%8F%91%E9%82%AE%E4%BB%B6/

"""
准备工作：
授权。各邮箱大同小异。这里qq邮箱为例。
qq邮箱首页/设置/账户  向下翻到POP3/IMAP/SMTP/服务。
"""
"""
邮件相关协议：
- SMTP(simple mail transfer protocol) 简单邮件传输协议。用于发邮件。
- POP3(Post office protocol) 邮局协议。将邮件服务器上资料同步到本地。用于收邮件。     开通以上两种协议后收邮件，发现可以正常收取，但有个问题，通过程序拉取的邮件已下载已阅读，但登录邮箱后发现下载的邮件仍然是未读状态。说明POP3协议只能简单地收件但不能标记邮件状态。
- IMAP(internet mail access protocol),交互式邮件存取协议，POP3协议的增强版。标记已读、删除，跟官方邮件服务器状态保持同步，体验较好。
- SSL，数据链路层加密，https基于此技术。qq邮箱的邮件协议也开启了这个加密，代码中注意配置SSL为True。
"""
"""
发邮件的包：
- smtplib poplib imaplib
1417633855@qq.com
snhoakptaidkgaeb
imap.qq.com 993
smtp.qq.com  465或587
"""
import yagmail
import os

sender ='1417633855@qq.com'
password ='snhoakptaidkgaeb' # 授权密码
target ='1315686027@qq.com'

yag=yagmail.SMTP(user=sender,password=password,host='smtp.qq.com',smtp_ssl=True)
contents = '傻狗'
yag.send(to=target,subject='来自小米的邮件',contents=contents)
print('发送成功')



