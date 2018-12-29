import requests

url ='http://news.163.com/'
print(requests.get(url).text)