# request包
# urllib偏底层  参数编码  修改seragent或使用proxy时需几行代码来进行构造操作，获得相应后

import requests

# GET请求 无参数
response=requests.get('http://www.baidu.com')
# print(response.status_code)
# print('\n\n\n\n',response.content)#content 2进制原始字符串
# print('\n\n\n\n',response.text) # 解码后的字符串

# 有参数  会自动把参数base64解码
resp=requests.get('http://www.baidu.com',params={'kw':'学习'})
print(resp)
print('\n\n\n\n',resp.text)

# 添加自定义请求信息headers
headers ={
 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
}
requests.get('http://www.baidu.com',headers=headers)

# post
params={'username':'张三','address':'郑州'}
requests.post('http://www.baidu.com',params=params)

# 代理
proxies ={
  'http':'http;//{}:{}'.format('185.132.133.107','8571')
}
requests.get('www.baidu.com',headers=headers,proxies=proxies)