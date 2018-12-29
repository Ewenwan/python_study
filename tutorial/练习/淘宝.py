import requests
from lxml import etree
import lxml.html
from urllib.request import urlretrieve
from CrawlerUtility import ChromeHeaders2Dict

taobao_url='https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2018.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E9%9B%B6%E9%A3%9F%E5%A4%A7%E7%A4%BC%E5%8C%85&suggest=0_1&_input_charset=utf-8&wq=%E9%9B%B6%E9%A3%9F&suggest_query=%E9%9B%B6%E9%A3%9F&source=suggest&fs=1&globalbuy=1&cps=yes&ppath=21299%3A27772'
header = """
:authority: s.taobao.com
:method: GET
:path: /search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2018.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E9%9B%B6%E9%A3%9F%E5%A4%A7%E7%A4%BC%E5%8C%85&suggest=0_1&_input_charset=utf-8&wq=%E9%9B%B6%E9%A3%9F&suggest_query=%E9%9B%B6%E9%A3%9F&source=suggest&fs=1&globalbuy=1&cps=yes&ppath=21299%3A27772
:scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: no-cache
cookie: thw=cn; cna=1N0XFMcjaCsCAXWgjJmdOyfU; miid=901425892106221713; t=f517682a48bd24b6390e683474b9e521; v=0; cookie2=14683743cbc0240457bb334561e92cd3; _tb_token_=55e8fee8beb60; unb=2994955639; sg=%E5%97%AF9f; _l_g_=Ug%3D%3D; skt=0778ad7298c8d29e; cookie1=BxeGkmP60bxKk1FUBWXWW9TwDlXCjqHeLoeqnrNG1H0%3D; csg=af3f89a7; uc3=vt3=F8dByRMHjgqUR%2FI8Pbk%3D&id2=UUGrcttDtR2J0g%3D%3D&nk2=piH3d3b3bCPkykKi&lg2=WqG3DMC9VAQiUQ%3D%3D; existShop=MTU0NTg4NDgyMg%3D%3D; tracknick=%5Cu54E6%5Cu54E61999%5Cu55EF%5Cu55EF; lgc=%5Cu54E6%5Cu54E61999%5Cu55EF%5Cu55EF; _cc_=W5iHLLyFfA%3D%3D; dnk=%5Cu54E6%5Cu54E61999%5Cu55EF%5Cu55EF; _nk_=%5Cu54E6%5Cu54E61999%5Cu55EF%5Cu55EF; cookie17=UUGrcttDtR2J0g%3D%3D; tg=0; enc=z83fIu2tmmCBcteHW1G0VrEpHVV2Ff1lf6lRRnTwaoSG3u3KfzFoaGN2WOqH3bhb0aXJxDl4Vy%2BCXARHmzg66Q%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie21=VFC%2FuZ9aiKCaj7AzMHh1&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&pas=0&cookie14=UoTYM86P9gChoQ%3D%3D&tag=8&lng=zh_CN; mt=ci=0_1; swfstore=174757; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; whl=-1%260%260%261545893457382; JSESSIONID=8FE34D7EA8F1A817CE35D3FB8BC59749; l=aB5EaxaxyiPwgSQmbMaJHspAG70jnOZPVEyF1May0TEhNtrwkeCXjjno-VwRj_qC5JCy_K-5F; isg=BNXVBEgUJTC61Ab4KMtqcmBH5NFPelTCC_7YiFd6kcybrvWgHyKZtONsfPK9rqGc
pragma: no-cache
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36
"""
headers =ChromeHeaders2Dict(header)
html = requests.get(taobao_url, headers=headers).text
# print(html)


tree = lxml.html.fromstring(html)
pattern_img_src = '//*[@id="J_Itemlist_Pic_584320461125"]/@src'

img = tree.xpath('//*[@id="mainsrp-related"]/div/dl/dt/text()')
print(img)
