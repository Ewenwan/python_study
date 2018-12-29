import json
import requests
url ='https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv8135&productId=100000177764&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
html =requests.get(url).text
# print(html[26:-2])
dict = json.loads(html[26:-2])
print(dict)
for i in dict['comments']:
    print(f"用户的名字是:{i['nickname']}\n用户的评价是{i['content']}")



