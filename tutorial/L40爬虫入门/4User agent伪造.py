import random
def get_random_user_agent():
  user_agent_list=[
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
 'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
  ]
  return  random.choice(user_agent_list)

print(get_random_user_agent())
user_agent=get_random_user_agent()
import urllib.request
rep=urllib.request.Request('http://www.baidu.com', data={'wd':'搜索关键字'} )
rep.add_header('User_Agent',user_agent)
resp=urllib.request.urlopen(rep)
print(resp)
html = resp.read().decode('utf-8')
print(html)                                                                   

from  fake_useragent import UserAgent
ua=UserAgent()
print(ua.random)
