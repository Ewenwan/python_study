# encoding:utf-8
import requests
import  re
import urllib.request
from fake_useragent import UserAgent

url ='https://www.newyx.net/gl/lolbjgs/'

headers={
    'UserAgent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
}
a=requests.get(url,headers=headers).text
print(a)
c=re.compile(r'<p class="text".>(.*?)</p>.*?',re.S)
b=re.findall(c,a)
print(b)


