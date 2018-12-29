import requests
proxies = {'http': 'http://119.101.112.120:9999'}
try:
    html = requests.get('http://www.ivsky.com/tupian/ziranfengguang/', proxies=proxies)
    print(html.text)
except Exception as e:
    print(e)
else:
    print('可用')
